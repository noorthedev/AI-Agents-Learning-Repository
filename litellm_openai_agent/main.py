#!/usr/bin/env python3
"""
03_litellm_openai_agent/main.py
A tiny "agent-style" loop using LiteLLM's OpenAI-compatible API.
We keep it simple: ask the model to reason "step-by-step" (no tools) and produce an answer.
Docs: https://docs.litellm.ai/
"""
import os
from litellm import completion

# Choose a provider/model.
# If you have an OpenAI key set as OPENAI_API_KEY, you can use: "openai/gpt-4o-mini"
# You can also route to an OpenRouter model via LiteLLM by setting
# OPENROUTER_API_KEY and model="openrouter/meta-llama/llama-3.1-8b-instruct:free"
MODEL = os.getenv("LITELLM_MODEL", "openai/gpt-4o-mini")

# LiteLLM will pick up provider API keys from env, e.g., OPENAI_API_KEY or OPENROUTER_API_KEY.
question = "Plan a 3-bullet study strategy to learn uv, OpenRouter, and LiteLLM."

resp = completion(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a concise, practical tutor."},
        {"role": "user", "content": question},
    ],
)

# Access content in an OpenAI-like way
msg = resp.choices[0].message
print(msg.get("content") or msg.get("message", ""))
