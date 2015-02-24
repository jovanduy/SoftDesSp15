# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Jordan Van Duyne

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq
DNA = load_seq("./data/X73525.fa")
from itertools import chain

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'

    Added tests for T and G just in case.
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """
    # TODO: implement this   <--Delete unncessary code for final turn in
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G':'C'}
    return complements[nucleotide]


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
        I assume that these two tests are already good enough; this function
        either works or does not work (there are no alternate types of situations 
        to test).
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this
    reverse_complement=''
    for i in range(len(dna)):
        reverse_complement = get_complement(dna[i]) + reverse_complement
    return reverse_complement

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'

    Added test without stop codon to see if it prints the entire string.
    >>> rest_of_ORF("ATGAAATTTAGAA")
    'ATGAAATTTAGAA'
    """
    # TODO: implement this
    orf = dna[0:3]
    i = 3
    while i < len(dna): #While loops are cool, but for loops are better because we can avoid infinite loops
        codon = dna[i:i+3]
        if (codon == 'TAG') or (codon == 'TAA') or (codon == 'TGA'):
            return orf #break works, but you could also just return
        orf += codon
        i += 3
    return orf


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']

    Added a test with a nested ORF to make sure it only returns non-nested ORFs.
    >>> find_all_ORFs_oneframe("ATGATGCATGAATGTAGATAGATGTGCCC")
    ['ATGATGCATGAATGTAGA', 'ATGTGCCC']
    """
    # TODO: implement this
    orfs = []
    i = 0
    while i < len(dna):
        if dna[i:i+3] == 'ATG':
            orf = rest_of_ORF(dna[i:])
            orfs.append(orf)
            i += len(orf)
        else:
            i += 3
    return orfs


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
        I assume this test is sufficent because it has ORFs in all three frames.
        Nested ORFs were already checked for in find_all_ORFs_oneframe, which this
        function calls.
    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    # TODO: implement this
    orfs = []
    for i in range(3):
        orf_list = find_all_ORFs_oneframe(dna[i:])
        for j in range(len(orf_list)):
            orfs.append(orf_list[j])
    return orfs
    
def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
        I assume this test is sufficient because it creates an ORF both from the
        original dna strand and the reverse complement strand.
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    orfs = find_all_ORFs(dna)
    orfs += find_all_ORFs(get_reverse_complement(dna))
    return orfs


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'

    Since the given test has the longest ORF on the reverse strand, I included a test
    in which the longest ORF is in the original strand.
    >>> longest_ORF("TTTGATGCTACATTCGCAT")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    ORFs = find_all_ORFs_both_strands(dna)
    longest = ORFs[0]
    for i in range(len(ORFs)):
        if len(ORFs[i]) > len(longest):
            longest = ORFs[i]
    return longest


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF
        No unit test because you can't know what it will return since dna is
        randomly shuffled each time you call this function. However, I did test
        it by having it print the length of the longest ORF in each trial it ran
        and then print the return value of longest_ORF_noncoding to make sure that
        it returns the length of the longest ORF over all trials (and it passed 
        this test).
    """
    length = 0
    for i in range(num_trials):
        shuffled = longest_ORF(shuffle_string(dna))
        if len(shuffled) > length:
            length = len(shuffled)
    return length

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'

        I added a test to make sure the function behaves correctly when there is
        one more nucleotide than a multiple of three in the input ORF (the first 
        test's input ORF has length that is a multiple of 3, the second test's input 
        has length of a multiple of three plus two, while this third test's input 
        will have length of a multiple of three plus one).  <--Nice!
        
        >>> coding_strand_to_AA("ATGCCCGCTT")
        'MPA'
    """
    # TODO: implement this
    AAs = ''
    for i in range(0, len(dna), 3):
        if len(dna)/3.0 != 0:
            if i >= len(dna) - 2:
                break
        AAs += aa_table[dna[i:i+3]]
    return AAs

def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    # TODO: implement this
    threshold = longest_ORF_noncoding(dna, 1500)
    all_ORFs = find_all_ORFs_both_strands(dna)
    AAs = []
    for i in range(len(all_ORFs)):
        orf = all_ORFs[i]
        if len(orf) > threshold:
            AAs.append(coding_strand_to_AA(orf))
    return AAs


if __name__ == "__main__":
    print gene_finder(DNA)
    import doctest
    doctest.testmod()
