#### n8n books

The .txt files contain workflows you can copy and paste into 
n8n-langchain-beta.

You need to edit the prompts in the pdf_book_to_article_with_langchain_example,
right now they use a book on api's to generate how to articles. But your
imagination is the limit.

Make sure to edit the regex in the code block that says split by
chapter, with a text identifier that splits the chapters, if you need
help you can ask for it on the forum over at ponx.ai. Don't clutter the
repo with issues.

If you want to use the epub workflow you need to use the helper script
to extract the text to json. It doesn't contain any langchain flows for
now it's just a basic workflow to help you with loading epubs into
langchain.
