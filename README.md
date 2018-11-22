# emmorph2conll

The script converts the output tag of emMorph morphological analyzer to the corresponding tag of a version Szeged Treebank.

# What's in this repo?

* the main script of the converter: `converter.py`
* three auxiliary scripts in folder `converterdata`
* full list of emMorph tags in folder `tagsets` TODO
* a table of CoNLL tags in folder `tagsets` TODO
* license
* this readme

# The tagsets :hungary:

## emMorph

[emMorph](https://github.com/dlt-rilmta/emMorph) is the current morphological analyzer for Hungarian and it is integrated into the [e-magyar](http://e-magyar.hu/en) language processing toolchain. The list of emMorph tags is from [here](http://e-magyar.hu/en/textmodules/emmorph_codelist).

## MSD

What we call here CoNLL is a modified version of the morphosyntactic tagset of [MULTEXT](http://nl.ijs.si/ME/Vault/V3/msd/msd.pdf) transformed into a feature-value pair structure. This modified tagset is an annotation scheme for a version of the largest fully manually annotated corpus of Hungarian, [Szeged Treebank](http://rgai.inf.u-szeged.hu/index.php?lang=en&page=SzegedTreebank).

# How to use the converter?

* standard input: token, lemma, emmorph tag separated by tab
* standard output: conll tag

# Dependencies

`Python3`

# License

GNU General Public License v3.0

# Our converters

* [emmorph2ud](https://github.com/vadno/emmorph2ud)
* [emmorph2msd](https://github.com/vadno/emmorph2msd)
