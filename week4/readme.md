TODO: Reflect on what you learned this week and what is still unclear.

python ../course/week4/tests.py

### Exercise 1:
    get_some_details
        - data["results"][0]["name"]["last"]
        this accesses the data, into results then name then last
        - need to follow the sequence of Json files

    wordy_pyramid
        problems: every word was formatted with a b in front e.g. "b'quacksalver'". This b needed to be removed, use the .split ("'")function to split the output into individual parts and select the second part to isolate the word
        
        .content pulls the word from the website and makes it a string
        .split = split a string into a list where each word is a list item
        .extent = adds all elements of an iterable list to the end of the list
        .reverse = revereses elemnts of the list

    pokedex
        status_code is 200 (means okay)
        status_code is 404 (means error)

    diarist
        .count() : counts the number of times a certain item occurs
        I followed the IOexmaples to make the code but had to look at other people's code for the LOCAL part

### Data Project - Invalid Option
    NYC Children's PlayGround/Park data
        number of columns: 18
            GISpropNum: String (letter and number) 
                GIS = geographic information system
            OMPpropID: String (letter and number)
            Accessibility: Boolean
            Accessibility Level: String
            Additional Location Info: String
            Additional Name Info: String
            Grp (group?): Integer
            Location: String
            Name: String
            Park District: String (letter and number)
            Point (Coordinates): Point
            Rules: String
            Zip Code: Integer
            Community Districts: Integer
            Borough Boundaries: Integer
            City Council Districts: Integer
            Polic Precincts: Integer

        number of rows: 945
        
        Borough Codes:
            Richmond/Staten Island - R - 1
            Brooklyn - B - 2
            Queens - Q - 3
            Manhattan - M - 4
            Bronx - X - 5

        General Details:
        - published by the City of New York 
        - Angency - Department of Parks and Recreation (DPR)
        - created by NYC Parks’ Innovation and Performance Management
        - purpose was to generate a dataset of Childrens Play Areas from NYC parks
        - created 8 April 2020, updated June 3 2020

        Sources:
        https://catalog.data.gov/dataset/childrens-play-areas-cpas
        https://github.com/NYC-Parks/ChildrensPlayAreas_public
        https://data.cityofnewyork.us/Recreation/Open-Space-Parks-/g84h-jbjm
        https://docs.google.com/spreadsheets/d/1wLCAPdqDYPh8fHiURSdd3v7-7WcbqxkWkUbbD29mm9Y/edit#gid=1896407081
        https://data.cityofnewyork.us/dataset/Children-s-Play-Areas-CPAs-/j55h-3upk

        Edit: I did some random checks on the data and determined that the zip codes were incorrect and leading also other incorrect location data e.g. polic precinct

 ### Data Project - Second Option       
    I liked the idea of looking at playgrounds and LA had similar data

    Source 1:  https://catalog.data.gov/dataset/department-of-recreation-and-parks-facility-and-park-information-e7cff 
        
        Rows: 986

        Columns: 22
            LocationType: String e.g. park, camps
            Location Name: String
            StNumber: Integer
            StNumberFraction: Integer (only contains one entry)
            StDirection: Letter
            StName: String
            StSuffix: String
            StSuffixDirection: Letter (only contains one entry)
            AddressType: String (only contains one entry)
            AddressTypeValue: integer(only contains one entry)
            CrossStDirection: no input
            CrossStName: integer	
            CrossStSuffix: string
            CrossStSuffixDirection: no input
            City: string
            State: string
            Zip: integer	
            Website: string	
            Phone: string of numbers
            CouncilDistrict: integer
            GeoLat: float	
            GeoLong: float

        Details:
            Created on 4/12/2013
            Updated on 24/4/2019
            Data owner is the Mayors office

        Things to look at
            Median age and type of recreational facility

    Source 2: https://data.lacity.org/dataset/2010-Census-Populations-by-Zip-Code/nxs9-385f 
        Rows: 319
        Columns: 7
            Zip Code: integer
            total population: integer
            median age: integer
            total males: integer
            total female: integer
            total households: integer
            average household size: integer

        Details:
            US 2010 Census owned by US Gov and Mayors Office

        Things to look at:
            compare both sets of data to determine correlation

