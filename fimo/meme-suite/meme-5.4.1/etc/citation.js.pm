# Do not edit this file.  It is created from etc/citation.js.
package Citation;
sub cite {
  my ($pgm) = @_;
  return $citation{$pgm};
}
%citation = (
"AMA" => "If you use this program in your research, please cite:\n\nFabian A. Buske, Mikael Boden, Denis C. Bauer and Timothy L. Bailey,\n\"Assigning roles to DNA regulatory motifs using comparative genomics\",\nBioinformatics, 26(7), 860-866, 2010.\n",
"AME" => "If you use this program in your research, please cite:\n\nRobert C. McLeay and Timothy L. Bailey,\n\"Motif Enrichment Analysis: a unified framework and an evaluation on ChIP data\",\nBMC Bioinformatics, 11:165, 2010.\n",
"CentriMo" => "If you use this program in your research, please cite:\n\nTimothy L. Bailey and Philip Machanick,\n\"Inferring direct DNA binding from ChIP-seq\",\nNucleic Acids Research, 40:e128, 2012.\n",
"DREME" => "If you use this program in your research, please cite:\n\nTimothy L. Bailey,\n\"DREME: Motif discovery in transcription factor ChIP-seq data\",\nBioinformatics, 27(12):1653-1659, 2011.\n",
"FIMO" => "If you use this program in your research, please cite:\n\nCharles E. Grant, Timothy L. Bailey and William Stafford Noble,\n\"FIMO: Scanning for occurrences of a given motif\",\nBioinformatics 27(7):1017-1018, 2011.\n",
"GLAM2" => "If you use this program in your research, please cite:\n\nMartin C. Frith, Neil F. W. Saunders, Bostjan Kobe and Timothy L. Bailey,\n\"Discovering sequence motifs with arbitrary insertions and deletions\",\nPLoS Computational Biology, 4(5):e1000071, 2008.\n",
"GLAM2SCAN" => "If you use this program in your research, please cite:\n\nMartin C. Frith, Neil F. W. Saunders, Bostjan Kobe and Timothy L. Bailey,\n\"Discovering sequence motifs with arbitrary insertions and deletions\",\nPLoS Computational Biology, 4(5):e1000071, 2008.\n",
"GOMo" => "If you use this program in your research, please cite:\n\nFabian A. Buske, Mikael Boden, Denis C. Bauer and Timothy L. Bailey,\n\"Assigning roles to DNA regulatory motifs using comparative genomics\",\nBioinformatics, 26(7), 860-866, 2010.\n",
"MAST" => "If you use this program in your research, please cite:\n\nTimothy L. Bailey and Michael Gribskov,\n\"Combining evidence using p-values: application to sequence homology searches\",\nBioinformatics, 14(1):48-54, 1998.\n",
"MCAST" => "If you use this program in your research, please cite:\n\nTimothy Bailey and William Stafford Noble,\n\"Searching for statistically significant regulatory modules\",\nBioinformatics (Proceedings of the European Conference on Computational Biology),\n19(Suppl. 2):ii16-ii25, 2003.\n",
"MetaMEME" => "If you use this program in your research, please cite:\n\nWilliam N. Grundy, Timothy L. Bailey, Charles P. Elkan and Michael E. Baker.\n\"Meta-MEME: Motif-based Hidden Markov Models of Protein Families\"\nComputer Applications in the Biological Sciences (CABIOS),\n13(4):397-406, 1997.\n",
"MEME" => "If you use this program in your research, please cite:\n\nTimothy L. Bailey and Charles Elkan,\n\"Fitting a mixture model by expectation maximization to\ndiscover motifs in biopolymers\",\nProceedings of the Second International Conference on Intelligent Systems\nfor Molecular Biology, pp. 28-36, AAAI Press, Menlo Park, California, 1994.\n",
"MEMEChIP" => "If you use this program in your research, please cite:\n\nPhilip Machanick and Timothy L. Bailey,\n\"MEME-ChIP: motif analysis of large DNA datasets\",\nBioinformatics 27(12):1696-1697, 2011.\n",
"MEME_SUITE" => "If you use this program in your research, please cite:\n\nTimothy L. Bailey, James Johnson, Charles E. Grant, William S. Noble,\n\"The MEME Suite\",\nNucleic Acids Research, 43(W1):W39-W49, 2015.\n",
"MoMo" => "If you use this program in your research, please cite:\n\nAlice Cheng, Charles Grant, Timothy L. Bailey and William Noble,\n\"MoMo: Discovery of statistically significant post-translational modification motifs\", \nBioinformatics, 35(16):2774-2782, 2018.\n",
"PSPs" => "If you use this program in your research, please cite:\n\nTimothy L. Bailey, Mikael Boden, Tom Whitington and Philip Machanick,\n\"The value of position-specific priors in motif discovery using MEME\",\nBMC Bioinformatics, 11(1):179, 2010.\n",
"SEA" => "If you use this program in your research, please cite:\n\nTimothy L. Bailey and Charles E. Grant, \"SEA: Simple Enrichment Analysis of motifs\",\nBioRxiv, 2021.\n",
"SpaMo" => "If you use this program in your research, please cite:\n\nTom Whitington, Martin C. Frith, James Johnson and Timothy L. Bailey\n\"Inferring transcription factor complexes from ChIP-seq data\",\nNucleic Acids Res. 39(15):e98, 2011.\n",
"STREME" => "If you use this program in your research, please cite:\n\nTimothy L. Bailey,\n\"STREME: accurate and versatile sequence motif discovery\",\nBioinformatics, Mar. 24, 2021.\n",
"Tomtom" => "If you use this program in your research, please cite:\n\nShobhit Gupta, JA Stamatoyannopolous, Timothy Bailey and William Stafford Noble,\n\"Quantifying similarity between motifs\",\nGenome Biology, 8(2):R24, 2007.\n",
"TGene" => "If you use this program in your research, please cite:\n\nTimothy O'Connor, Charles E. Grant, Mikael Boden, Timothy L. Bailey,\n\"T-Gene: Improved target gene prediction\",\nBioinformatics, 36(12):3902-3904, 2020.\n",
"XSTREME" => "If you use this program in your research, please cite:\n\nCharles E. Grant and Timothy L. Bailey, \"XSTREME: comprehensive motif analysis of biological sequence datasets\",\nBioRxiv, 2021.\n",
);
