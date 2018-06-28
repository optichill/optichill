# Data Filtering

The purpose of this markdown file is to describe the use cases for implementing the chiller plant data filtering and preparation programs.

### Software dependencies

```
pandas
numpy
glob
os
```

There are two key functions in this program. One of them is `import_and_filter`, which is designed to import a list of plant filenames, filter the data contained in them, and output them as a pandas dataframe. The second is `train_single_plt`, which uses `import_and_filter` to generate a test-train split based on user specified testing and training plant data.