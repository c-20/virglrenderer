#!/usr/bin/env python

'''
/**************************************************************************
 *
 * Copyright 2009-2010 VMware, Inc.
 * All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sub license, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice (including the
 * next paragraph) shall be included in all copies or substantial portions
 * of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
 * IN NO EVENT SHALL VMWARE AND/OR ITS SUPPLIERS BE LIABLE FOR
 * ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 *
 **************************************************************************/

/**
 * @file
 * Pixel format packing and unpacking functions.
 *
 * @author Jose Fonseca <jfonseca@vmware.com>
 */
'''
from __future__ import print_function


from u_format_parse import *


def print_channels(format, func):
    if format.nr_channels() <= 1:
        func(format.le_channels, format.le_swizzles)
    else:
        print('#ifdef PIPE_ARCH_BIG_ENDIAN')
        func(format.be_channels, format.be_swizzles)
        print('#else')
        func(format.le_channels, format.le_swizzles)
        print('#endif')

def generate(formats):
    print()
    print('#include "pipe/p_compiler.h"')
    print('#include "u_math.h"')
    print('#include "u_half.h"')
    print('#include "u_format.h"')
    print()

