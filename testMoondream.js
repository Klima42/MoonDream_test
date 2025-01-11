import { vl } from "moondream";
import fs from "fs";

// Initialize the client with your API key
const model = new vl({
  apiKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlfaWQiOiIyZWM5MGIxNS05ZmEzLTRlOGItOTBkNS0zMzMxODgwMzMwYzMiLCJpYXQiOjE3MzY1MjYzMzd9.BCq0LcyeGyGYWCPQiuD0fiVxfi0UYanWy0dEWHYBo2M", // Replace with your actual API key
});

// Read an image file
const image = fs.readFileSync("C:\\traitement\\ai_image\\moondream_env\\lol.jpg");



async function main() {
  // Generate a caption for the image
  const caption = await model.caption({
    image: image,
    length: "normal",
    stream: false,
  });
  console.log("Caption:", caption);

  // Ask a question about the image
  const answer = await model.query({
    image: image,
    question: "What's can you see in this image ?",
    stream: false,
  });
  console.log("Answer:", answer);
}

main();
