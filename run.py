#!/usr/bin/env python3

from argparse import ArgumentParser
from brs_libs import rpSBML

if __name__ == "__main__":
    parser = ArgumentParser('Input source molecule')
    parser.add_argument('-sourcefile', type=str)
    parser.add_argument('-input_format', type=str)
    parser.add_argument('-target_sbml', type=str)
    parser.add_argument('-output', type=str)
    params = parser.parse_args()


    if input_format == 'sbml':
        rpmerge = rpSBML.mergeSBMLFiles(params.sourcefile, params.target_sbml, params.output)

    # with TemporaryDirectory() as tmpInputFolder:
    #     with TemporaryDirectory() as tmpOutputFolder:
    #         tar = tar_open(input_tar, 'r')
    #         tar.extractall(path=tmpInputFolder)
    #         tar.close()
    #         if len(glob(tmpInputFolder+'/*'))==0:
    #             logging.error('Input file is empty')
    #             return False
    #         for sbml_path in glob(tmpInputFolder+'/*'):
    #             '''
    #             rpsbml = rpSBML.rpSBML(file_name)
    #             rpsbml.readSBML(sbml_path)
    #             target_rpsbml = rpSBML.rpSBML(file_name)
    #             target_rpsbml.readSBML(target_sbml)
    #             rpmerge = rpMerge.rpMerge()
	# 			species_source_target, reactions_convert = rpmerge.mergeModels(rpsbml, rpsbml_gem)
    #             '''
    #
    #             file_name = sbml_path.split('/')[-1].replace('.sbml', '').replace('.xml', '').replace('.rpsbml', '').replace('_sbml', '').replace('_rpsbml', '')
    #             rpSBML.mergeSBMLFiles(sbml_path, target_sbml, tmpOutputFolder)
    #             os_replace(os_path.join(tmpOutputFolder, 'target.sbml'), os_path.join(tmpOutputFolder, file_name+'_sbml.xml'))
    #         if len(glob(tmpOutputFolder+'/*'))==0:
    #             logging.error('rpMergeSBML has generated no results')
    #             return False
    #         with tar_open(output_tar, mode='w:gz') as ot:
    #             for sbml_path in glob.glob(tmpOutputFolder+'/*'):
    #                 file_name = str(sbml_path.split('/')[-1].replace('.sbml', '').replace('.xml', '').replace('.rpsbml', '').replace('_sbml', '').replace('_rpsbml', ''))
    #                 info = tarfile.TarInfo(file_name+'_sbml.xml')
    #                 info.size = os_path.getsize(sbml_path)
    #                 ot.addfile(tarinfo=info, fileobj=open(sbml_path, 'rb'))
    return True
