#!/usr/bin/env python
#-*- coding:utf-8 -*-

top = '.'
out = 'pdf'


def configure(conf):
    conf.load('tex')
    if not conf.env.PDFLATEX:
        conf.fatal('Could not find pdflatex')
    conf.find_program('pygmentize', var='PYGMENTIZE')


def options(opt):
    opt.load('tex')


def build(bld):
    # first, run pygments on all code snippets:
    for suffix in ('.f90', '.pyx', '.py'):
        for blob in bld.path.ant_glob('Pygsnippets/*'+suffix):
            print blob.srcpath()
            bld(rule='${PYGMENTIZE} -P style=default -f tex -o ${TGT} ${SRC}',
                source=blob.nice_path(),
                target=blob.nice_path().replace(suffix, '.tex'))

    bld.add_group()

    bld(
            features = 'tex',
            type     = 'pdflatex',  # pdflatex or xelatex
            source   = 'talk.tex',  # mandatory, the source
            outs     = 'pdf',  # 'pdf' or 'ps pdf'
            prompt   = 0  # 0 for the batch mode
       )
