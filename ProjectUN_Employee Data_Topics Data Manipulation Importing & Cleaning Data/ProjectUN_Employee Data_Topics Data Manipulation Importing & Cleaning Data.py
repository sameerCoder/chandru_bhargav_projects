#!/usr/bin/env python
# coding: utf-8

# ## 1. Loading data from CSV and Excel files
# <p>You just got hired as the first and only data practitioner at a small business experiencing exponential growth. The company needs more structured processes, guidelines, and standards. Your first mission is to structure the human resources data. The data is currently scattered across teams and files and comes in various formats: Excel files, CSVs, JSON files, SQL databases…</p>
# <p>The Head of People Operations wants to have a general view gathering all available information about a specific employee. Your job is to gather it all in a file that will serve as the reference moving forward. You will merge all of this data in a pandas DataFrame before exporting to CSV.</p>
# <p>Data management at your company is not the best, but you need to start somewhere. You decide to tackle the most straightforward tasks first, and to begin by loading the company office addresses. They are currently saved into a CSV file, <code>office_addresses.csv</code>, which the Office Manager sent over to you. Additionally, an HR manager you remember interviewing with gave you access to the Excel file, <code>employee_information.xls</code>, where the employee addresses are saved. You need to load these datasets in two separate DataFrames.</p>

# In[ ]:


# Import the library you need

# Load office_addresses.csv
df_office_addresses = ...

# Load employee_information.xls
df_employee_addresses = ...

# Take a look at the first rows of the DataFrames
print(...)
print(...)


# In[ ]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\n# One or more tests of the student\'s code\n# The @solution should pass the tests\n# The purpose of the tests is to try to catch common errors and\n# to give the student a hint on how to resolve these errors\n\ncorrect_office_addresses = pd.read_csv("datasets/office_addresses.csv")\ncorrect_employee_addresses = pd.read_excel("datasets/employee_information.xls")\n\ndef test_office_addresses():\n    assert correct_office_addresses.equals(df_office_addresses), \\\n    "It seems your there\'s something wrong with your `df_office_addresses` DataFrame.\\n\\\n     Are you sure you loaded the `office_addresses.csv` located in the `datasets` folder\\n\\\n     using pandas `read_csv()` method?"\n    \ndef test_employee_addresses():\n    assert correct_employee_addresses.equals(df_employee_addresses), \\\n    "It seems your there\'s something wrong with your `df_employee_addresses` DataFrame.\\n\\\n     Are you sure you loaded `employee_addresses.csv` located in the `datasets` folder\\n\\\n     using pandas `read_excel()` method?"')


# ## 2. Loading employee data from Excel sheets
# <p>It turns out the <code>employee_information.xls</code> file also holds information about emergency contacts for each employee in a second sheet titled <code>emergency_contacts</code>. However, this sheet was edited at some points, and the header was removed! Looking at the data, you were able to figure out what the header should be, and you confirmed that they were appropriate with the HR manager: <code>employee_id</code>, <code>last_name</code>, <code>first_name</code>, <code>emergency_contact</code>, <code>emergency_contact_number</code>, <code>relationship</code>.</p>

# In[ ]:


# Load data from the second sheet of employee_information.xls
df_emergency_contacts = ...

# Declare a list of new column names
emergency_contacts_header = ...

# Rename the columns
df_emergency_contacts.columns = ...

...


# In[ ]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\n# One or more tests of the student\'s code\n# The @solution should pass the tests\n# The purpose of the tests is to try to catch common errors and\n# to give the student a hint on how to resolve these errors\n\ncorrect_emergency_contacts = pd.read_excel("datasets/employee_information.xls", sheet_name=1, header=None)\ncorrect_emergency_contacts_header = ["employee_id", "last_name", "first_name",\n                             "emergency_contact", "emergency_contact_number", "relationship"]\ncorrect_emergency_contacts.columns = correct_emergency_contacts_header\n\n\ndef test_emergency_headers():\n    correct_emergency_contacts_header == emergency_contacts_header\n    "It seems there\'s something wrong with your `emergency_contacts_header` list.\\n\\\n     Are you sure you used the column names provided by the HR manager?"\n\ndef test_emergency_columns():\n    correct_emergency_contacts.columns == df_emergency_contacts.columns\n    "It seems there\'s something wrong with your DataFrame\'s column titles.\\n\\\n     Are you sure you used the list storing column names provided by the HR manager?"\n    \ndef test_emergency_contacts():\n    assert correct_emergency_contacts.equals(df_emergency_contacts), \\\n    "It seems there\'s something wrong with your `df_emergency_contacts` DataFrame.\\n\\\n     Are you sure you loaded `employee_information.xls` located in the `datasets` folder\\n\\\n     using pandas `read_excel()` method, specifying the correct sheet\\n\\\n     and paying attention to the state of the headers?"')


# ## 3. Loading role data from JSON files
# <p>All right, you're making good progress! Now the next step is to gather information about employee roles, teams, and salaries. This information usually lives in a human resources management system, but the Head of People Operations exported the data for you into a JSON file titles <code>employee_roles.json</code>.</p>
# <p>Looking at the JSON file, you see entries are structured in a specific way. It is built as a Python dictionary: the keys are employee IDs, and each employee ID has a corresponding dictionary value holding role, salary, and team information. Here are the first few lines of the file:</p>
# <pre><code>{"001":
#   {
#     "title": "CEO",
#     "monthly_salary": "$4500",
#     "team": "Leadership"
#   },
#  ...
# }
# </code></pre>
# <p>Load the JSON file to a variable <code>df_employee_roles</code>, choosing the appropriate orientation.</p>

# In[ ]:


# Load employee_roles.json
df_employee_roles = ...
df_employee_roles = df_employee_roles.reindex(sorted(df_employee_roles.columns), axis=1)

# Take a look at the first rows of the DataFrame
df_employee_roles.head()


# In[ ]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\n# One or more tests of the student\'s code\n# The @solution should pass the tests\n# The purpose of the tests is to try to catch common errors and\n# to give the student a hint on how to resolve these errors\n\ncorrect_employee_roles = pd.read_json("datasets/employee_roles.json", orient="index")\ncorrect_employee_roles = correct_employee_roles.reindex(sorted(correct_employee_roles.columns), axis=1)\n\nrecords_employee_roles = pd.read_json("datasets/employee_roles.json", orient="records")\n\ndef test_records_orient():\n    assert not records_employee_roles.reindex(sorted(records_employee_roles.columns), axis=1)\\\n               .equals(df_employee_roles.reindex(sorted(df_employee_roles.columns), axis=1)), \\\n    "It seems you used the \'records\', \'columns\' or \'values\' orientation.\\n\\\n     This puts the employee ID as column titles\\n\\\n     and the employee title, monthly salary and team as the index.\\n\\\n     You want the other way around: employee ID as index\\n\\\n     and title, monthly salary and team as the column titles.\\n\\\n     Try another `orient` value!"\n\ndef test_employee_roles():\n    assert correct_employee_roles.equals(df_employee_roles), \\\n    "It seems there\'s something wrong with your `df_employee_roles` DataFrame.\\n\\\n     Are you sure you loaded `employee_roles.json` located in the `datasets` folder\\n\\\n     using pandas `read_json()` method, specifying the correct orientation?"')


# ## 4. Merging several DataFrames into one
# <p>You now have all the data required! All that's left is bringing it all in a unique DataFrame. This unique DataFrame will enable the Head of People Operations to access all employee data at once.</p>
# <p>In this step, you will merge all DataFrames. In the next step, you will remove duplicates and reorganize the columns - don't worry about this for now.</p>

# In[ ]:


# Merge df_emergency_contacts with df_employee_addresses
df_employees = df_employee_addresses...(..., how="left", on=..., copy=False)

# Merge df_employee_roles with df_employees
df_employees = df_employees...(..., how="left", left_on=..., right_on=..., copy=False)

# Merge df_office_adresses with df_employees
df_employees = df_employees...(..., how="left", left_on=..., right_on=..., copy=False)

# Take a look at the first rows of the DataFrame and its columns
print(...)
print(...)


# In[ ]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\n# One or more tests of the student\'s code\n# The @solution should pass the tests\n# The purpose of the tests is to try to catch common errors and\n# to give the student a hint on how to resolve these errors\n\n# Task 1\ncorrect_office_addresses = pd.read_csv("datasets/office_addresses.csv")\n\ncorrect_employee_addresses = pd.read_excel("datasets/employee_information.xls")\n\n# Task 2\ncorrect_emergency_contacts = pd.read_excel("datasets/employee_information.xls", sheet_name=1, header=None)\ncorrect_emergency_contacts_header = ["employee_id", "last_name", "first_name",\n                             "emergency_contact", "emergency_contact_number", "relationship"]\ncorrect_emergency_contacts.columns = correct_emergency_contacts_header\n\n# Task 3\ncorrect_employee_roles = pd.read_json("datasets/employee_roles.json", orient="index")\ncorrect_employee_roles = correct_employee_roles.reindex(sorted(correct_employee_roles.columns), axis=1)\n\n# Task 4\ncorrect_employees = correct_employee_addresses.merge(correct_emergency_contacts,\n                                                     how="left",\n                                                     on="employee_id")\ncorrect_employees = correct_employees.merge(correct_employee_roles,\n                                            how="left", \n                                            left_on="employee_id",\n                                            right_on=correct_employee_roles.index)\ncorrect_employees = correct_employees.merge(correct_office_addresses,\n                                            how="left",\n                                            left_on="employee_country",\n                                            right_on="office_country")\n\ndef test_index_length():\n    assert len(correct_employees.index) == len(df_employees.index), \\\n    "It looks like your DataFrame does not have the right count of columns.\\n\\\n     Be careful not to change the merge method used (\\"left\\"), as other methods might drop rows."\n\ndef test_column_length():\n    assert len(correct_employees.columns) == len(df_employees.columns), \\\n    "It looks like your DataFrame does not have the right count of columns.\\n\\\n     You should end up with 20 columns."\n    \ndef test_column_titles():\n    assert correct_employees.columns.to_list().sort() == df_employees.columns.to_list().sort(), \\\n    "It looks like your DataFrame does not have the right columns titles.\\n\\\n     Here is the column index you should end up with:\\n\\\n     `[\'employee_id\', \'employee_last_name\', \'employee_first_name\',\\n\\\n       \'employee_country\', \'employee_city\', \'employee_street\',\\n\\\n       \'employee_street_number\', \'last_name\', \'first_name\',\\n\\\n       \'emergency_contact\', \'emergency_contact_number\', \'relationship\',\\n\\\n       \'monthly_salary\', \'team\', \'title\', office\', \'office_country\',\\n\\\n       \'office_city\', \'office_street\', \'office_street_number\']`."\n\ndef test_employees():\n    assert correct_employees.equals(df_employees), \\\n    "It seems there\'s something wrong with your `df_employees` DataFrame.\\n\\\n     Are you sure you merged all the DataFrames in the order specified?\\n\\\n     You should always use a left join here."')


# ## 5. Editing column names
# <p>Now that you merged all of your DataFrames into one let's make sure we have the information required by People Ops.</p>
# <p>Currently, your <code>df_employees</code> DataFrame has the following column titles:
# <code>employee_id</code>, <code>employee_last_name</code>, <code>employee_first_name</code>, <code>employee_country</code>, <code>employee_city</code>, <code>employee_street</code>, <code>employee_street_number</code>, <code>last_name</code>, <code>first_name</code>, <code>emergency_contact</code>, <code>emergency_contact_number</code>, <code>relationship</code>, <code>monthly_salary</code>, <code>team</code>, <code>title</code>,  <code>office</code>, <code>office_country</code>, <code>office_city</code>, <code>office_street</code>, <code>office_street_number</code>.</p>
# <p>The columns <code>employee_last_name</code> and <code>last_name</code> are duplicates. The columns <code>employee_first_name</code> and <code>first_name</code> are duplicates as well. On top of this, People Ops wants to rename some of the columns:</p>
# <ul>
# <li><code>employee_id</code> should be <code>id</code></li>
# <li><code>employee_country</code> should be <code>country</code></li>
# <li><code>employee_city</code> should be <code>city</code></li>
# <li><code>employee_street</code> should be <code>street</code></li>
# <li><code>employee_street_number</code> should be <code>street_number</code></li>
# </ul>
# <p>So your header should look like this in the end:
# <code>id</code>, <code>country</code>, <code>city</code>, <code>street</code>, <code>street_number</code>, <code>last_name</code>, <code>first_name</code>, <code>emergency_contact</code>, <code>emergency_number</code>, <code>emergency_relationship</code>, <code>monthly_salary</code>, <code>team</code>, <code>title</code>, <code>office</code>, <code>office_country</code>, <code>office_city</code>, <code>office_street</code>, <code>office_street_number</code>.</p>

# In[ ]:


# Drop the columns
df_employees_renamed = ...

# Declare a list of new columns names and rename the DataFrame columns
new_header = [...]

# Rename the columns
df_employees_renamed.columns = ...

# Take a look at the first rows of the DataFrame
...


# In[ ]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\n# One or more tests of the student\'s code\n# The @solution should pass the tests\n# The purpose of the tests is to try to catch common errors and\n# to give the student a hint on how to resolve these errors\n\n# Task 1\ncorrect_office_addresses = pd.read_csv("datasets/office_addresses.csv")\n\ncorrect_employee_addresses = pd.read_excel("datasets/employee_information.xls")\n\n# Task 2\ncorrect_emergency_contacts = pd.read_excel("datasets/employee_information.xls", sheet_name=1, header=None)\ncorrect_emergency_contacts_header = ["employee_id", "last_name", "first_name",\n                                     "emergency_contact", "emergency_contact_number", "relationship"]\ncorrect_emergency_contacts.columns = correct_emergency_contacts_header\n\n# Task 3\ncorrect_employee_roles = pd.read_json("datasets/employee_roles.json", orient="index")\ncorrect_employee_roles = correct_employee_roles.reindex(sorted(correct_employee_roles.columns), axis=1)\n\n# Task 4\ncorrect_employees = correct_employee_addresses.merge(correct_emergency_contacts,\n                                                     how="left",\n                                                     on="employee_id")\ncorrect_employees = correct_employees.merge(correct_employee_roles,\n                                            how="left", \n                                            left_on="employee_id",\n                                            right_on=correct_employee_roles.index)\ncorrect_employees = correct_employees.merge(correct_office_addresses,\n                                            how="left",\n                                            left_on="employee_country",\n                                            right_on="office_country")\n\n# Task 5\ncorrect_employees_renamed = correct_employees.drop(["employee_first_name", "employee_last_name"], axis=1)\ncorrect_header = ["id", "country", "city", "street", "street_number", "last_name", "first_name",\n                  "emergency_contact", "emergency_number", "emergency_relationship",\n                  "monthly_salary", "team", "title", "office", "office_country", \n                  "office_city", "office_street", "office_street_number"]\ncorrect_employees_renamed.columns = correct_header\n\nprint(correct_employees_renamed.head())\n\ndef test_column_name():\n    assert correct_header == new_header, \\\n    "It seems your `new_column_names` is incorrect.\\n\\\n     Are you sure you used the column names given by People Ops,\\n\\\n     in the order they were provided?\\n\\\n     Make sure there\'s no typo."\n    \ndef test_employees_renamed():\n    assert correct_employees_renamed.equals(df_employees_renamed), \\\n    "It seems there\'s something wrong with your `df_employees_oredered` DataFrame.\\n\\\n     Are you sure you renamed the column titles and then reordered them?"')


# ## 6. Changing column order
# <p>Now that you have the appropriate column names, you can reorder the columns.</p>

# In[ ]:


# Declare a list for the new column's order and reorder columns
new_column_order = ...

# Reorder the columns
df_employees_ordered = ...

# Take a look at the result
df_employees_ordered.head()


# In[ ]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\n# One or more tests of the student\'s code\n# The @solution should pass the tests\n# The purpose of the tests is to try to catch common errors and\n# to give the student a hint on how to resolve these errors\n\n# Task 1\ncorrect_office_addresses = pd.read_csv("datasets/office_addresses.csv")\n\ncorrect_employee_addresses = pd.read_excel("datasets/employee_information.xls")\n\n# Task 2\ncorrect_emergency_contacts = pd.read_excel("datasets/employee_information.xls", sheet_name=1, header=None)\ncorrect_emergency_contacts_header = ["employee_id", "last_name", "first_name",\n                             "emergency_contact", "emergency_contact_number", "relationship"]\ncorrect_emergency_contacts.columns = correct_emergency_contacts_header\n\n# Task 3\ncorrect_employee_roles = pd.read_json("datasets/employee_roles.json", orient="index")\ncorrect_employee_roles = correct_employee_roles.reindex(sorted(correct_employee_roles.columns), axis=1)\n\n# Task 4\ncorrect_employees = correct_employee_addresses.merge(correct_emergency_contacts,\n                                                     how="left",\n                                                     on="employee_id")\ncorrect_employees = correct_employees.merge(correct_employee_roles,\n                                            how="left", \n                                            left_on="employee_id",\n                                            right_on=correct_employee_roles.index)\ncorrect_employees = correct_employees.merge(correct_office_addresses,\n                                            how="left",\n                                            left_on="employee_country",\n                                            right_on="office_country")\n\n# Task 5\ncorrect_employees_renamed = correct_employees.drop(["employee_first_name", "employee_last_name"], axis=1)\ncorrect_header = ["id", "country", "city", "street", "street_number", "last_name", "first_name",\n                  "emergency_contact", "emergency_number", "emergency_relationship",\n                  "monthly_salary", "team", "title", "office", "office_country", \n                  "office_city", "office_street", "office_street_number"]\ncorrect_employees_renamed.columns = correct_header\n\n# Task 6\ncorrect_column_order = ["id", "last_name", "first_name", "title", "team", "monthly_salary", \n                        "country", "city", "street", "street_number",\n                        "emergency_contact", "emergency_number", "emergency_relationship",\n                        "office", "office_country", "office_city", "office_street", "office_street_number"]\ncorrect_employees_ordered = correct_employees_renamed[correct_column_order]\n\ndef test_column_order():\n    assert correct_column_order == new_column_order, \\\n    "It seem your `new_column_names` is incorrect.\\n\\\n     Are you sure you used the column names given by People Ops,\\n\\\n     in the order they were provided?\\n\\\n     Make sure there\'s no typo."\n    \ndef test_employees_renamed():\n    assert correct_employees_ordered.equals(df_employees_ordered), \\\n    "It seems there\'s something wrong with your `df_employees_oredered` DataFrame.\\n\\\n     Are you sure you renamedthe column titles and then reordered them?."')


# ## 7. The last minute request
# <p>Last touches! You were ready to let People Ops know that the DataFrame was ready, but the department head just went over to your desk after lunch, asking about some last-minute requirements.</p>
# <p>Let's polish the DataFrame before exporting the data, sending it over to People Ops, and deploying the pipeline:</p>
# <ul>
# <li>All street numbers should be integers</li>
# <li>The index should be the actual employee ID rather than the row number</li>
# <li>If the value for office is <code>NaN</code> then the employee is remote: add a column named "status", right after <code>monthly_salary</code> indicating whether the employee is "On-site" or "Remote."</li>
# </ul>

# In[ ]:


# Reset the index and drop the column
df_employees_final = ...

status_list = []

# Loop through the row values and append to status_list accordingly
for ..., ... in ...:
    if ...:
        ...
    else:
        ...

# Insert status_list as a new column
df_employees_final.insert(...)

# Take a look at the first rows of the DataFrame
df_employees_final.head()


# In[ ]:


get_ipython().run_cell_magic('nose', '', '# %%nose needs to be included at the beginning of every @tests cell\n\n# One or more tests of the student\'s code\n# The @solution should pass the tests\n# The purpose of the tests is to try to catch common errors and\n# to give the student a hint on how to resolve these errors\n\n# Task 1\ncorrect_office_addresses = pd.read_csv("datasets/office_addresses.csv")\n\ncorrect_employee_addresses = pd.read_excel("datasets/employee_information.xls")\n\n# Task 2\ncorrect_emergency_contacts = pd.read_excel("datasets/employee_information.xls", sheet_name=1, header=None)\ncorrect_emergency_contacts_header = ["employee_id", "last_name", "first_name",\n                             "emergency_contact", "emergency_contact_number", "relationship"]\ncorrect_emergency_contacts.columns = correct_emergency_contacts_header\n\n# Task 3\ncorrect_employee_roles = pd.read_json("datasets/employee_roles.json", orient="index")\ncorrect_employee_roles = correct_employee_roles.reindex(sorted(correct_employee_roles.columns), axis=1)\n\n# Task 4\ncorrect_employees = correct_employee_addresses.merge(correct_emergency_contacts,\n                                                     how="left",\n                                                     on="employee_id")\ncorrect_employees = correct_employees.merge(correct_employee_roles,\n                                            how="left", \n                                            left_on="employee_id",\n                                            right_on=correct_employee_roles.index)\ncorrect_employees = correct_employees.merge(correct_office_addresses,\n                                            how="left",\n                                            left_on="employee_country",\n                                            right_on="office_country")\n\n# Task 5\ncorrect_employees_renamed = correct_employees.drop(["employee_first_name", "employee_last_name"], axis=1)\ncorrect_header = ["id", "country", "city", "street", "street_number", "last_name", "first_name",\n                  "emergency_contact", "emergency_number", "emergency_relationship",\n                  "monthly_salary", "team", "title", "office", "office_country", \n                  "office_city", "office_street", "office_street_number"]\ncorrect_employees_renamed.columns = correct_header\n\n# Task 6\ncorrect_column_order = ["id", "last_name", "first_name", "title", "team", "monthly_salary", \n                        "country", "city", "street", "street_number",\n                        "emergency_contact", "emergency_number", "emergency_relationship",\n                        "office", "office_country", "office_city", "office_street", "office_street_number"]\ncorrect_employees_ordered = correct_employees_renamed[correct_column_order]\n\n# Task 7\ncorrect_employees_final = correct_employees_ordered.set_index(correct_employees_ordered["id"]).drop(columns=["id"])\n\ncorrect_status = []\nfor index, row in correct_employees_final.iterrows():\n    if pd.isnull(row["office"]):\n        correct_status.append("Remote")\n    else:\n        correct_status.append("On-site")\n\ncorrect_employees_final.insert(loc=5, column="status", value=correct_status)\n\ndef test_status():\n    assert correct_status == status_list, \\\n    "It seems `status_list` is not correct.\\n\\\n     Make sure you\'re looping through the rows of the `df_employees_final` DataFrame.\\n\\\n     You should append \'Remote\' to `status` if the value is `NaN` and \'On-site\' otherwise."\n    \ndef test_employees_final():\n    assert correct_employees_final.equals(df_employees_final), \\\n    "It seems your `df_employees_final` DataFrame is not correct.\\n\\\n     Are you sure you added your `status_list` as the 5th column?"')


# ## 8. Saving your work
# <p>Good job! You now have everything People Ops requested. The different people responsible for these various files can currently keep working on these files if they want. As long as they save it in the <code>datasets</code> folder, People Ops will have to execute this unique script to obtain just one file from the ones scattered across different teams.</p>
# <p>You bumped into the Head of People Ops and shared a few caveats and areas of improvement. She booked a meeting with you so you can explain:</p>
# <ul>
# <li>How the current structure isn't robust to role changes: what if an existing employee takes on a new role?</li>
# <li>How the current structure doesn't fit best practices in terms of database schema:<ul>
# <li>having data all over the place like it's the case right now is a no-go</li>
# <li>but gathering everything in a single table is inefficient: you have to query all information even if all you want is a phone number</li>
# <li>there should be a single SQL database for employee data, with several tables that can be joined</li>
# <li>views can be built on top of the database to simplify non-data practitioners access.</li></ul></li>
# </ul>
# <p>In any case, you still need to show up with what was requested - so let's export your DataFrame to a CSV file.</p>

# In[ ]:


# Write to CSV


# In[ ]:


get_ipython().run_cell_magic('nose', '', '\n# Task 1\ncorrect_office_addresses = pd.read_csv("datasets/office_addresses.csv")\n\ncorrect_employee_addresses = pd.read_excel("datasets/employee_information.xls")\n\n# Task 2\ncorrect_emergency_contacts = pd.read_excel("datasets/employee_information.xls", sheet_name=1, header=None)\ncorrect_emergency_contacts_header = ["employee_id", "last_name", "first_name",\n                             "emergency_contact", "emergency_contact_number", "relationship"]\ncorrect_emergency_contacts.columns = correct_emergency_contacts_header\n\n# Task 3\ncorrect_employee_roles = pd.read_json("datasets/employee_roles.json", orient="index")\ncorrect_employee_roles = correct_employee_roles.reindex(sorted(correct_employee_roles.columns), axis=1)\n\n# Task 4\ncorrect_employees = correct_employee_addresses.merge(correct_emergency_contacts,\n                                                     how="left",\n                                                     on="employee_id")\ncorrect_employees = correct_employees.merge(correct_employee_roles,\n                                            how="left", \n                                            left_on="employee_id",\n                                            right_on=correct_employee_roles.index)\ncorrect_employees = correct_employees.merge(correct_office_addresses,\n                                            how="left",\n                                            left_on="employee_country",\n                                            right_on="office_country")\n\n# Task 5\ncorrect_employees_renamed = correct_employees.drop(["employee_first_name", "employee_last_name"], axis=1)\ncorrect_header = ["id", "country", "city", "street", "street_number", "last_name", "first_name",\n                  "emergency_contact", "emergency_number", "emergency_relationship",\n                  "monthly_salary", "team", "title", "office", "office_country", \n                  "office_city", "office_street", "office_street_number"]\ncorrect_employees_renamed.columns = correct_header\n\n# Task 6\ncorrect_column_order = ["id", "last_name", "first_name", "title", "team", "monthly_salary", \n                        "country", "city", "street", "street_number",\n                        "emergency_contact", "emergency_number", "emergency_relationship",\n                        "office", "office_country", "office_city", "office_street", "office_street_number"]\ncorrect_employees_ordered = correct_employees_renamed[correct_column_order]\n\n# Task 7\ncorrect_employees_final = correct_employees_ordered.set_index(correct_employees_ordered["id"]).drop(columns=["id"])\n\ncorrect_status = []\nfor index, row in correct_employees_final.iterrows():\n    if pd.isnull(row["office"]):\n        correct_status.append("Remote")\n    else:\n        correct_status.append("On-site")\n\ncorrect_employees_final.insert(loc=5, column="status", value=correct_status)\n\ndf_employees_final.to_csv("final.csv")\n\ncorrect_csv = pd.read_csv("final.csv")\nstudent_csv = pd.read_csv("employee_data.csv")\n\ndef test_csv():\n    assert correct_csv.equals(student_csv), \\\n    "It seems your CSV file is not correct.\\n\\\n     Make sure your `df_employees_final` DataFrame is correct,\\n\\\n     and that it\'s the one you\'re exporting to CSV."')

