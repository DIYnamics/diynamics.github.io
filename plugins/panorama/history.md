# Changes history

## 0.2.1

- Updated to be compliant with the latest versions of dependencies

## 0.2.0

- Added `lineChart` support configured by default to display time series
- Added `count_article_by_month` that count the number of articles by month
- Added the ability to display time series (and especially in `lineChart`
- Added [tox](https://testrun.org/tox/latest/) configuration
- Fixed a hack in the chart display
- Fixed a misuse of the `pivot_table` in `count_article_by_column_by_year` 
- Fixed the URL of the dependencies in the test page template

## 0.1.1

- Refactoring some code for simplification
    - use of `DataFrame` instead of `dict` of `Series`
    - use `pivot_table` for better clarity

## 0.1.0

- First push to GitHub