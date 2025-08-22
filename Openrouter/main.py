#!/usr/bin/env python3
"""
02_openrouter/main.py
Minimal OpenRouter chat completion example with robust error handling.
"""
import os
import sys
import json
import requests

def main():
    API_KEY = os.getenv("OPENROUTER_API_KEY")
    if not API_KEY:
        print("Error: Please set OPENROUTER_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        # Content-Type will be set automatically by requests when using json=...
    }

    payload = {
        "model": "openrouter/auto",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say a one-sentence greeting!"}
        ],
        "max_tokens": 150,
        "temperature": 0.2,
    }

    try:
        # use json= so requests sets Content-Type automatically
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e, file=sys.stderr)
        sys.exit(1)

    # Helpful debug info if something goes wrong
    if not resp.ok:
        print(f"OpenRouter returned HTTP {resp.status_code}", file=sys.stderr)
        try:
            print(resp.json(), file=sys.stderr)
        except Exception:
            print(resp.text, file=sys.stderr)
        sys.exit(1)

    try:
        data = resp.json()
    except ValueError:
        print("Response is not JSON:", resp.text, file=sys.stderr)
        sys.exit(1)

    # Try multiple common response shapes (OpenAI-like and some OpenRouter variants)
    assistant_text = None
    # 1) OpenAI-like: choices[0].message.content
    try:
        assistant_text = data["choices"][0]["message"]["content"]
    except Exception:
        assistant_text = None

    # 2) Alternative: choices[0].text
    if assistant_text is None:
        try:
            assistant_text = data["choices"][0].get("text")
        except Exception:
            pass

    # 3) 'output' shaped responses (some providers / structured outputs)
    if assistant_text is None and "output" in data:
        try:
            out = data["output"]
            if isinstance(out, list) and len(out) > 0:
                first = out[0]
                # common nested shapes
                if isinstance(first, dict):
                    c = first.get("content") or first.get("text")
                    if isinstance(c, list) and len(c) > 0:
                        # content is list of {"type":"output_text","text": "..."} or similar
                        candidate = c[0]
                        assistant_text = candidate.get("text") or candidate.get("content") or str(candidate)
                    elif isinstance(c, str):
                        assistant_text = c
                    else:
                        assistant_text = str(first)
                else:
                    assistant_text = str(first)
            else:
                assistant_text = str(out)
        except Exception:
            assistant_text = None

    # Fallback: print pretty JSON if we couldn't extract assistant text
    if assistant_text is None:
        print("Couldn't extract assistant text — full response below:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        print(assistant_text)

if __name__ == "__main__":
    main()
