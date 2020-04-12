from __future__ import division
import os
#import urllib, cStringIO
#import pymongo as pm ## first establish ssh tunnel to server where database is running
import base64
import numpy as np
from numpy import *
import PIL
from PIL import Image
import base64
import matplotlib
from matplotlib import pylab, mlab, pyplot
from IPython.core.pylabtools import figsize, getfigs
plt = pyplot
import seaborn as sns
sns.set_context('poster')
sns.set_style('white')
from matplotlib.path import Path
import matplotlib.patches as patches
import pandas as pd
from svgpathtools import parse_path, wsvg
from glob import glob
from IPython.display import clear_output


def list_files(path, ext='png'):
    result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.%s' % ext))]
    return result

def flatten(x):
    return [val for sublist in x for val in sublist]

def make_svg_list(stroke_recs):
    '''
    grab sample drawing's strokes and make a list of svg strings from it
    '''
    svg_list = []
    for single_stroke in stroke_recs:
        svg_string = single_stroke['svgData']
        svg_list.append(svg_string)
    return svg_list

def render_svg(paths,
               stroke_width = 5,
               stroke_linecap = 'round',
               stroke_color = 'black',
               fill_mode = 'none',
               viewbox=[0, 0, 300, 300],
               base_dir = './',
               out_dir = 'svg_images',
               out_fname= 'tmp.svg'):

    '''
    see docs for wsvg: https://www.pydoc.io/pypi/svgpathtools-1.3.3/autoapi/paths2svg/index.html?highlight=wsvg#paths2svg.wsvg
    wsvg(paths=None, colors=None, filename=join, stroke_widths=None, nodes=None, node_colors=None, node_radii=None, openinbrowser=False, timestamp=False, margin_size=0.1, mindim=600, dimensions=None, viewbox=None, text=None, text_path=None, font_size=None, attributes=None, svg_attributes=None)
    '''

    ## render out to svg file
    #print('Rendering out to {}'.format(os.path.join(out_dir,out_fname)))
 
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    wsvg(paths,
         attributes=[{'stroke-width':stroke_width,
                      'stroke-linecap':stroke_linecap,
                      'stroke':stroke_color,
                      'fill':fill_mode}]*len(paths),
         viewbox=viewbox,
         filename=os.path.join(base_dir,out_dir,out_fname))
    
def render_svg_color(paths,
                     stroke_colors,
               stroke_width = 4,
               stroke_linecap = 'round',
               fill_mode = 'none',
               viewbox=[0, 0, 300, 300],
               base_dir = './',
               out_dir = 'svg_images',
               out_fname= 'tmp.svg'):

    '''
    see docs for wsvg: https://www.pydoc.io/pypi/svgpathtools-1.3.3/autoapi/paths2svg/index.html?highlight=wsvg#paths2svg.wsvg
    wsvg(paths=None, colors=None, filename=join, stroke_widths=None, nodes=None, node_colors=None, node_radii=None, openinbrowser=False, timestamp=False, margin_size=0.1, mindim=600, dimensions=None, viewbox=None, text=None, text_path=None, font_size=None, attributes=None, svg_attributes=None)
    '''

    ## render out to svg file
    print('Rendering out to {}'.format(os.path.join(out_dir,out_fname)))
   
    if not os.path.exists(os.path.join(base_dir,out_dir)):
        os.makedirs(os.path.join(base_dir,out_dir))
    wsvg(paths,
         attributes=[{'stroke-width':stroke_width,
                      'stroke-linecap':stroke_linecap,
                      'stroke':color,
                      'fill':fill_mode} for color in stroke_colors],
         viewbox=viewbox,
         filename=os.path.join(base_dir,out_dir,out_fname))
 


def generate_svg_path_list(svg_dir):
    svg_paths = list_files(svg_dir, ext='svg')
    svg_paths = [i for i in svg_paths if i != '.DS_Store']
    return svg_paths

def svg_to_png(svg_paths,
               base_dir = './',
               out_dir = 'png_images'):
    '''
    svg_paths: list of paths to svg files
    '''
    if not os.path.exists(os.path.join(base_dir,out_dir)):
        os.makedirs(os.path.join(base_dir,out_dir))
    for path in svg_paths:
        out_path = os.path.join(base_dir,out_dir,'{}.png'.format(path.split('/')[-1].split('.')[0]))
        ## running ImageMagick command 'convert' to convert svgs to pngs
        cmd_string = 'convert {} {}'.format(path,out_path)
        print(cmd_string)
        os.system(cmd_string)
        clear_output(wait=True)
        
        




