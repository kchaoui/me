TODO: Reflect on what you learned this week and what is still unclear.

As part of my data project, I need to find further data on the land area per zip code. While looking as the minimum values and googling them, it appeared that the zip code with a very low population and park count had a low land area. To normalize the data, I need to either normalize it to find parks per 10000 people or parks per 1 km^2

Also I should look into mapping county locations on a map, and a breakdown of facilities per zip code as a stacked bar chart and also an outdoor/indoor

* there are many different options that can be used when creating graphs including altering the labels, x/y ticks, titles and other elements.
* plt.rc creates global changed to the file so all plots have the same e.g. font size
* lambda functions made it very straightforward to clean my data
* the same principles that add columns to dataframes do not necessarily work for geodata frames
* plain text can be added to annotate graphs, this was really helpful when I wanted to create my own legend titles:
        \n plt.text(x, y, 'text', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=10, family='avenir next')
* printing out the full table:
        \n  with pd.option_context('display.max_rows', None, 'display.max_columns', None): 
        \n   print(dfmerged_data) 
* some forms of plotting work better when the index is part of the dataset and other do not, I needed to use the .copy function to duplicate the dataset and make changes without altering the original. I struggled a lot with this section before I learnt about .copy because when I would change the index, all of my plots would work except one and vice versa.


I wanted to make a tree map with subcategories but to have it with the same colour format as I have currently, this would be quite complex to do as only plot.ly can create this. The following code did not work as intended:
            fig = px.treemap(categorised, 
                 path=['Category', 'Location Type'], 
                 values='Facility Counts',
                 color_discrete_sequence=stackedcolour)