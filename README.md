# Batch Manga Bundler

This is a Python script that is used to batch manga chapters together. It copies all `.jpg` files from a source directory into a new directory with filenames incremented from `001.jpg`. After all the files have been copied and renamed, it prompts the user for metadata (title, author, and summary), creates a `ComicInfo.xml` metadata file, and bundles all the files into a `.cbz` (Comic Book Zip) file.

## Folder Structure

Here is an example of how your project directory could look like:

```bash
.
├── script.py
├── source
│   ├── Chapter1
│   │   ├── 01.jpg
│   │   ├── 02.jpg
│   │   └── 03.jpg
│   ├── Chapter2
│   │   ├── 01.jpg
│   │   ├── 02.jpg
│   │   └── 03.jpg
│   └── Chapter3
│       ├── 01.jpg
│       ├── 02.jpg
│       └── 03.jpg
└── output

```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need Python 3 installed on your system. If you don't have Python installed you can find it [here](https://www.python.org/downloads/).

### Installation

Clone the repository:

```bash
git clone https://github.com/jslyonnais/manga-images-chapter-batcher.git
cd manga-images-chapter-batcher
```

### Usage

1. Prepare your source directory with the `.jpg` files you want to bundle.

2. Run the script:

```bash
python script.py
```

If you want to see debug information, you can use the `--debug` flag:

```bash
python script.py --debug
```

The script will prompt you for the title, author, and summary for the `.cbz` file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
