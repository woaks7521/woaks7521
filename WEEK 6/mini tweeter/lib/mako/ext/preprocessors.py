# ext/preprocessors.py
# Copyright (C) 2006-2014 the Mako authors and contributors <see AUTHORS file>
#
# This module is part of Mako and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""preprocessing functions, used with the 'preprocessor' 
argument on Template, TemplateLookup"""

import re

def convert_comments(text):
    """preprocess old style comments.
 
    example:
 
    from mako.ext.preprocessors import convert_comments
    t = Template(..., preprocessor=preprocess_comments)"""
    return re.sub(r'(?<=\n)\s*#[^#]', "##", text)

