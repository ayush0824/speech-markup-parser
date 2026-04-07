# SSML Runtime Engine

Deterministic SSML parsing, validation, serialization, and caching utilities for production-grade text-to-speech and GenAI speech pipelines.

## Overview

SSML Runtime Engine is a lightweight Python project that implements a hand-rolled SSML parser, serializer, and runtime cache without relying on external XML parsing libraries. It is designed to validate, structure, and serialize SSML safely for text-to-speech workflows, especially in systems where deterministic output and strict input validation matter.

This project also includes an O(1) LRU cache to reduce repeated parsing and serialization overhead in runtime speech pipelines.

## Why this project matters

In AI and GenAI systems, especially text-to-speech applications, prompt integrity and deterministic formatting are critical. A malformed SSML prompt can break synthesis, produce inconsistent outputs, or create downstream debugging issues.

This project addresses that by:

- enforcing strict SSML structure and attribute validation
- generating deterministic serialized output for reproducibility
- safely handling XML character escaping and unescaping
- reducing repeated computation through efficient caching

## Impact

This project demonstrates how to build a small but production-relevant runtime layer for speech systems:

- **Improves reliability** by rejecting malformed SSML before it reaches a TTS engine
- **Supports reproducibility** through deterministic serialization and stable attribute ordering
- **Reduces repeated runtime overhead** with an O(1) LRU cache for parsed structures
- **Strengthens GenAI/TTS pipelines** by adding a guardrail layer between generated text and speech synthesis

## Features

- Hand-rolled SSML tokenizer and parser in Python
- Abstract syntax tree style representation using `SSMLTag` and `SSMLText`
- Deterministic SSML serializer
- Strict attribute parsing and validation
- XML escaping and unescaping support
- O(1) LRU cache using hashmap + doubly linked list
- Full unit test coverage for the required functionality

## Technical Highlights

### SSML Parser
The parser:
- tokenizes raw SSML into text, start-tag, and end-tag tokens
- validates structure such as a single top-level `<speak>` root
- rejects malformed attributes and mismatched tags
- supports parsing nested SSML nodes into a tree representation

### Deterministic Serialization
The serializer:
- converts parsed nodes back into valid SSML
- preserves structure in a predictable format
- sorts attributes for stable output across runs

### LRU Cache
The cache:
- supports O(1) `get`, `set`, and `has`
- tracks recency with a doubly linked list
- evicts the least recently used item when capacity is exceeded

## Example Use Cases

- validating LLM-generated SSML before sending it to a speech engine
- building a runtime layer for TTS orchestration systems
- ensuring deterministic prompt serialization in speech evaluation pipelines
- reducing repeated parse overhead in high-frequency synthesis workflows

## Tech Stack

- Python 3
- Standard Library only
- Unit Testing

## Project Structure

```bash
src/
  lru.py
  ssml.py
  tests/
