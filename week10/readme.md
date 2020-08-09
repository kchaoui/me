TODO: Reflect on what you learned this week and what is still unclear.

As part of my data project, I need to find further data on the land area per zip code. While looking as the minimum values and googling them, it appeared that the zip code with a very low population and park count had a low land area. To normalize the data, I need to either normalize it to find parks per 10000 people or parks per 1 km^2

Also I should look into mapping county locations on a map, and a breakdown of facilities per zip code as a stacked bar chart and also an outdoor/indoor

* there are many different options that can be used when creating graphs including altering the labels, x/y ticks, titles and other elements.
* plt.rc creates global changed to the file so all plots have the same e.g. font size
* lambda functions made it very straightforward to clean my data
* the same principles that add columns to dataframes do not necessarily work for geodata frames
* plain text can be added to annotate graphs, this was really helpful when I wanted to create my own legend titles:
        plt.text(x, y, 'text', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=10, family='avenir next')
* printing out the full table:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(dfmerged_data) 
* some forms of plotting work better when the index is part of the dataset and other do not, I needed to use the .copy function to duplicate the dataset and make changes without altering the original


