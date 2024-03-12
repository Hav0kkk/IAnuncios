### IAnuncios PoC 0.1

Roadmap:

- Crawl from source > generates raw text and images

$ wget resource > raw.txt images.jpg

- Enrich with LLM > generates the script

$ curl chatgpt api "raw.txt" > speech.txt 

- Text to speech > generate the audio

$ TTS speech.txt > audio.mp3

- Attach images to the audio > generates video

$ videomaker audio.mp3 images.jpg > video.mp4

- Upload to server > generates link

https://www.youtube.com/@IAnuncios

- Create SN posts > generates traffic


