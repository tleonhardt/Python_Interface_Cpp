#!/usr/bin/env python
# coding=utf-8
""" pytest unit test for the SWIG wrapper for compressing and decompressing
using the fastlz C library.
"""
import numpy as np
from Compress import VectorUint8, Compress, Decompress


def test_compress_and_decompress_roundtrip():
    # Beginning of the United States Constitution
    text ="""We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.

Article I (Article 1 - Legislative)
Section 1
All legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives.

Section 2
1: The House of Representatives shall be composed of Members chosen every second Year by the People of the several States, and the Electors in each State shall have the Qualifications requisite for Electors of the most numerous Branch of the State Legislature.

2: No Person shall be a Representative who shall not have attained to the Age of twenty five Years, and been seven Years a Citizen of the United States, and who shall not, when elected, be an Inhabitant of that State in which he shall be chosen.

3: Representatives and direct Taxes shall be apportioned among the several States which may be included within this Union, according to their respective Numbers, which shall be determined by adding to the whole Number of free Persons, including those bound to Service for a Term of Years, and excluding Indians not taxed, three fifths of all other Persons.2  The actual Enumeration shall be made within three Years after the first Meeting of the Congress of the United States, and within every subsequent Term of ten Years, in such Manner as they shall by Law direct. The Number of Representatives shall not exceed one for every thirty Thousand, but each State shall have at Least one Representative; and until such enumeration shall be made, the State of New Hampshire shall be entitled to chuse three, Massachusetts eight, Rhode-Island and Providence Plantations one, Connecticut five, New-York six, New Jersey four, Pennsylvania eight, Delaware one, Maryland six, Virginia ten, North Carolina five, South Carolina five, and Georgia three.

4: When vacancies happen in the Representation from any State, the Executive Authority thereof shall issue Writs of Election to fill such Vacancies.

5: The House of Representatives shall chuse their Speaker and other Officers; and shall have the sole Power of Impeachment."""

    # TODO: Convert the text to a VectorUint8 which can be passed to Compress

    # TODO: Create a vector to store the compressed data

    # Compress the input text
    success = Compress(text_vec, compressed_vec)
    assert success

    # Verify that the compressed text is actually smaller than the original
    assert len(compressed_vec) < len(text_vec)

    # TODO: Create a vector for the reconstructed text

    # Decmopress the compressed text to reconstruct a vector of original bytes
    success = Decompress(compressed_vec, recon_vec)
    assert success

    # TODO: Convert the reconstructed text to a bytes

    # TODO: And finally back to a str

    # Verify the reconstructed text is the same as the original
    assert text == reconstructed
