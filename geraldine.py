#!/usr/bin/env python
# coding: utf-8

# In[46]:


from IPython.display import HTML, display

# Define your HTML content as a string
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Management and Bill Payment Tracker</title>
</head>
<body>
    <h1>Welcome to Your Document Management and Bill Payment Tracker</h1>
    <img src="https://images.unsplash.com/photo-1517430816045-df4b7de11d1d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDJ8fGRlc2t8ZW58MHx8fHwxNjI4MDg1ODkz&ixlib=rb-1.2.1&q=80&w=400" width="320" height="240" alt="Organized Desk with Documents">
    <h3>Manage your bills, receipts, and financial documents with ease.</h3>
    
    <!-- Sign Up Form -->
    <h4>Sign Up</h4>
    <form action="/signup" method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Sign Up">
    </form>
    
    <!-- Sign In Form -->
    <h4>Sign In</h4>
    <form action="/signin" method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Sign In">
    </form>
</body>
</html>
"""

# Create an instance of HTML with the HTML content
html_display = HTML(html_content)

# Display the HTML
display(html_display)


# In[ ]:




