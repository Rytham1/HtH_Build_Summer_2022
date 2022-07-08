import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

vg_data = pandas.read_csv("Video_Games.csv")

print(vg_data)