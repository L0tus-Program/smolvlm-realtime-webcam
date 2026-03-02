# SmolVLM real-time camera demo

![demo](./demo.png)

This repository is a simple demo for how to use llama.cpp server with SmolVLM 500M to get real-time object detection

## Run everything with Docker Compose

1. Install Docker Desktop (or Docker Engine + Compose plugin).
2. Run:

```bash
docker compose up --build
```

3. Open `http://localhost:8080`.
4. Click `Start`.

The compose file starts:
- `web` (this frontend + reverse proxy)
- `llama-server` (SmolVLM via `llama.cpp`)
- `translator` (lightweight EN->PT translation API)

Note: translator uses online translation provider, so internet access is required for translation.

## Optional translation to Portuguese

- In the UI, enable `Translate response to PT-BR` to translate model output in real time.
- When disabled, output is shown in the original English.

## Manual run (without Compose)

If you prefer local binaries, run:

```bash
llama-server -hf ggml-org/SmolVLM-500M-Instruct-GGUF --jinja --chat-template smolvlm
```

## Troubleshooting

If you see:
`tokenize: error: number of bitmaps (1) does not match number of markers (0)`

Your server/chat template is not inserting the multimodal marker in the prompt. Make sure:

- You are using a recent `llama.cpp` build.
- You started `llama-server` with `--jinja --chat-template smolvlm`.

If translation is not ready yet:

```bash
docker compose ps
docker compose logs -f translator
```
