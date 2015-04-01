XML Sitemap Generator
=====================

XML sitemap generator, which given the list of URLs with specific priority level [high|medium|low], generates the XML sitemap for you.

How to use it?
==============

- You can run this python script like this:

$ python xml-generator.py [priority-level] [input-file-name]

- Priority level can be either high or medium or low (1st command line argument)

- Input file should be a simple text file with \n separated list of URLs to process

Where to put XML sitemap?
=========================

- Once XML sitemap files are generated for various priority levels, create a directory named "sitemap" in your root folder and put these files in this directory

- Now, edit sitemap_index.xml file, add your domain name in it and add this file in the root folder of your website

- That's it!

How to submit these files to various search engine bots?
========================================================

- You can directory add this index file (sitemap_index.xml) in google, bing etc. webmaster tools, it'll take care of all other files

- Also, you can link this index file from your robots.txt as well, by appending the following line:

Sitemap: http://www.example.com/sitemap_index.xml