#!/usr/bin/env python3
"""
00_swarm/demo.py
A tiny, zero-dependency "swarm" example. We simulate two agents:
- WeatherAgent: answers basic weather-like questions (mocked).
- MathAgent: does simple addition/multiplication.
A Router picks which agent to use based on keywords.
"""

import sys
from dataclasses import dataclass
from typing import Callable, Dict

@dataclass
class Message:
    role: str  # "user" or "assistant"
    content: str

class WeatherAgent:
    def handle(self, message: Message) -> str:
        # Mocked response (no external API!).
        # We just echo a pretend forecast.
        return "Mock Weather: Karachi, Today: 33°C, Humidity 65%, Light breeze."

class MathAgent:
    def handle(self, message: Message) -> str:
        text = message.content.lower()
        # A *very* tiny parser for "add A and B" / "multiply A and B"
        import re
        add = re.search(r"add\s+(-?\d+)\s+and\s+(-?\d+)", text)
        mul = re.search(r"(?:multiply|times)\s+(-?\d+)\s+(?:and|by)\s+(-?\d+)", text)
        if add:
            a, b = int(add.group(1)), int(add.group(2))
            return f"{a} + {b} = {a+b}"
        if mul:
            a, b = int(mul.group(1)), int(mul.group(2))
            return f"{a} * {b} = {a*b}"
        return "I can add or multiply. Try: 'Add 2 and 3' or 'Multiply 4 and 5'."

class Router:
    def __init__(self, agents: Dict[str, Callable[[Message], str]]):
        self.agents = agents

    def route(self, message: Message) -> str:
        text = message.content.lower()
        if any(k in text for k in ["weather", "temperature", "forecast"]):
            return self.agents["weather"](message)
        if any(k in text for k in ["add", "multiply", "times"]):
            return self.agents["math"](message)
        return "Not sure which agent to use. Ask a weather question or a small math question."

def main():
    user_input = " ".join(sys.argv[1:]) or "What's the weather?"
    msg = Message(role="user", content=user_input)
    weather_agent = WeatherAgent()
    math_agent = MathAgent()
    router = Router(
        agents={
            "weather": weather_agent.handle,
            "math": math_agent.handle,
        }
    )
    print(router.route(msg))

if __name__ == "__main__":
    main()
