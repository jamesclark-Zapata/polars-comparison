# Polars Comparison

## Get the data

* Visit the [gov.uk site](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads#single-file)
* Pick "the complete Price Paid Transaction Data as a CSV file (CSV, 4.3GB)".
* Add headers (see `headers.csv`)
```
cat headers.csv pp-complete.csv > price.csv
```

## Run

`python bench.py <implementation> <test case>`

## Implementations
* `pandas_naive`
* `pandas_opt` (`usecols` + `index`)
* `polars_naive`
* `polars_lazy`

## Test cases
* `n_sold`
* `price`
* `most_expensive`
