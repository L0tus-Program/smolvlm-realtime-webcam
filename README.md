# SmolVLM real-time camera demo

![demo](./demo.png)

This repository is a simple demo for how to use llama.cpp server with SmolVLM 500M to get real-time object detection

## How to setup

1. Install [llama.cpp](https://github.com/ggml-org/llama.cpp)
2. Run `llama-server -hf ggml-org/SmolVLM-500M-Instruct-GGUF --jinja --chat-template smolvlm`  
   Note: you may need to add `-ngl 99` to enable GPU (if you are using NVidia/AMD/Intel GPU)  
   Note (2): You can also try other models [here](https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md)
3. Open `index.html`
4. Optionally change the instruction (for example, make it returns JSON)
5. Click on "Start" and enjoy

## Troubleshooting

If you see:
`tokenize: error: number of bitmaps (1) does not match number of markers (0)`

Your server/chat template is not inserting the multimodal marker in the prompt. Make sure:

- You are using a recent `llama.cpp` build.
- You started `llama-server` with `--jinja --chat-template smolvlm`.
