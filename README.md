# SmolVLM real-time camera demo

![demo](./demo.png)

This repository is a simple demo for how to use llama.cpp server with SmolVLM 500M to get real-time object detection

## Run everything with Docker Compose

1. Install Docker Desktop (or Docker Engine + Compose plugin).
2. Install NVIDIA driver with Docker GPU support enabled (`nvidia-smi` must work on host).
3. Run:

```bash
docker compose up --build
```

4. Open `http://localhost:8080`.
5. Click `Start`.

The compose file starts:
- `web` (this frontend + reverse proxy)
- `llama-server` (SmolVLM via `llama.cpp` CUDA image)
- `translator` (lightweight EN->PT translation API)

To verify GPU is actually used:

```bash
docker compose exec -T llama-server ./llama-server --list-devices
docker compose logs llama-server
```

Expected: CUDA devices listed and logs mentioning CUDA backend / GPU offload.

Note: translator uses online translation provider, so internet access is required for translation.

## Optional translation to Portuguese

- In the UI, enable `Translate prompt PT-BR -> EN` to translate instruction before sending to model.
- In the UI, enable `Translate response to PT-BR` to translate model output in real time.
- When disabled, output is shown in the original English.
- `Translator: online/offline` shows translator availability.

## Token controls in UI

- `Max input tokens (approx)`: truncates instruction text before sending.
- `Max output tokens`: controls `max_tokens`/`n_predict` in model requests.

## Manual run (without Compose)

If you prefer local binaries, run:

```bash
llama-server -hf ggml-org/SmolVLM-500M-Instruct-GGUF --n-gpu-layers all
```

## Troubleshooting

If you see:
`tokenize: error: number of bitmaps (1) does not match number of markers (0)`

Your server/chat template is not inserting the multimodal marker in the prompt. Make sure:

- You are using a recent `llama.cpp` build.
- You started `llama-server` with a compatible chat template for your `llama.cpp` version.

If translation is not ready yet:

```bash
docker compose ps
docker compose logs -f translator
```
