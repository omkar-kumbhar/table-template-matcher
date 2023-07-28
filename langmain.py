import os
import numpy as np
import pandas as pd

class TemplateMatcherPrompts:
    system_prompt = """You are a CSV file understanding chatbot. You job is to
    assist an engineer for understanding content in csv files, and provide
    assistance in delivering high quality insights and code for given csv files.
    """

    template_prompt = """
    You are given two tables. `Table` and `Template`
    Your Job is to map values of `Table` to the given `Template` table and explain
    your rationale behind it. 

    Both `Table` and `Template` were loaded using pandas and then converted to a dictionary 
    using pd.read_csv(file_path).to_dict() where each `key` is associated with a column name.
    all keys are column values given to you in the form of a `row_number` and `value` mapping.

    `Template`:
    ```
    {test_template_element}
    ```

    `Table`:
    {test_table_element}

    Note:
    1. For each column in the `Template`, the system suggests columns from `Table` 
    (1 or more relevant candidates), showing the basis for the decision 
    (formats, distributions, and other features that are highlighted in the backend).

    2. Automatically generate data mapping code for each column display in the final Template format. 
    For example, for date columns, they may be in different formats, and it is necessary to change the order 
    from dd.mm.yyyy to mm.dd.yyyy. The person can check the code (or pseudocode) that will perform the mapping.
    
    3. Check that all data has been transferred correctly; if any errors occur, issue an alert to the person.


    At the end, please also provide code required for transformation in python. 
    If there are possible issues, please provide context. Assume that the inputs would 
    be template_csv_filepath and table_csv_filepath. 
    Return the transformed table as a pandas dataframe.

    Use the following output format:
    `Output Format`:
    
    ```
    `Reasoning for transformation`:
    <your reasnoing>
    
    `Code`:
     <code in python>

    `Transformed Table`:
    <transformed table>

    `Issues`:
    <Any particular issues>
    ```
    """


## Prompt Version 0.0 

# import os
# import numpy as np
# import pandas as pd

# class TemplateMatcherPrompts:
#     system_prompt = """You are a CSV file understanding chatbot. You job is to
#     assist an engineer for understanding content in csv files, and provide
#     assistance in delivering high quality insights and code for given csv files.
#     """

#     template_prompt = """
#     You are given two tables. `Table` and `Template`
#     Your Job is to map values of `Table` to the given `Template` table and explain
#     your rationale behind it. 

#     Both `Table` and `Template` were loaded using pandas and then converted to a dictionary 
#     using pd.read_csv(file_path).to_dict() where each `key` is associated with a column name.
#     all keys are column values given to you in the form of a `row_number` and `value` mapping.

#     Note:
#     For each column in the `Template`, the system suggests columns from `Table` 
#     (1 or more relevant candidates), showing the basis for the decision 
#     (formats, distributions, and other features that are highlighted in the backend).

#     At the end, please also provide code required for transformation in python. 
#     If there are possible issues, please provide context. Assume that the inputs would 
#     be template_csv_filepath and table_csv_filepath. 
#     Return the transformed table as a pandas dataframe.

#     `Template`:
#     ```
#     {test_template_element}
#     ```

#     `Table`:
#     {test_table_element}
#     """




