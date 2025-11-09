
# Book Memory Calculator

This Python program calculates how much memory is needed to store a book, including its **pictures, numbers, and text**. You can also convert the result into different units like bytes, KB, MB, etc.

## How It Works

1. **Pictures**

   * Ask if the book has pictures.
   * If yes, enter:

     * Number of pictures
     * Type of palette: RGB, CMYK, HighColor, Monochrome, or a custom palette
     * Width and height of each picture
   * Calculates memory needed for pictures.

2. **Numbers**

   * Ask if the book has numbers.
   * If yes, enter:

     * How many numbers
     * Base of numbers (like 2 for binary, 10 for decimal)
   * Calculates memory needed for numbers.

3. **Text**

   * Ask if the book has text.
   * If yes, enter:

     * Total number of characters
     * Alphabet type: ASCII, UNICODE, or a custom alphabet
   * Calculates memory needed for text.

4. **Total Memory**

   * Adds up the memory for pictures, numbers, and text.
   * You can convert it into other units like bytes, KB, MB, GB, or TB.

## Example Run

```
Do you have picture in your book? yes
How much? 5
Enter your palette(RGB, CMYK, HighColor, Monochrome or custom): RGB
Enter the length of picture(pixels): 100
Enter the width of picture(pixels): 200

Do you have numbers in your book? yes
How much? 10
Enter the base of your number: 10

Do you have text in your book? yes
Total number of characters: 1000
Enter alphabet type (ASCII, UNICODE, or number of letters): ASCII

Do you want it in another unit? yes
Which one (b, Kb, Mb, Gb, Tb)? Kb
```

Output:

```
Memory required: 12345 Kb
```

## Features

* Calculates memory for **pictures, numbers, and text**
* Supports **RGB, CMYK, HighColor, Monochrome, or custom palettes**
* Supports **ASCII, UNICODE, or custom alphabets**
* Converts memory into different units (b, KB, MB, GB, TB)

