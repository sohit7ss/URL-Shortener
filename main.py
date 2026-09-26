from flask import Flask, render_template, redirect, url_for, request
import random
import string


app = Flask(__name__)

shortened_urls = {}

