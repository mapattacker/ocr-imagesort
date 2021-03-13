# ocr-imagesort

I made this repository to help a friend sort her plant experiment images into respective folders according to their tag names. This is an example image below.

<img src="https://github.com/mapattacker/ocr-imagesort/blob/master/example-tag.jpg?raw=true" width=40% />

I was initially thinking of training an object detection model for the tags, then used an OCR library to phrase the tag. However, since there isn't any other characters in the images, I decided to just try using an OCR lib on the entire image.

I have tried several libraries, and [easyocr](https://github.com/JaidedAI/EasyOCR) appear to perform the best. However, to get fast predictions, I need to resize the images & use GPU.

Below is the workflow of this mini-project.

<img src="https://github.com/mapattacker/ocr-imagesort/blob/master/ocr-flow.png?raw=true" width=80% />