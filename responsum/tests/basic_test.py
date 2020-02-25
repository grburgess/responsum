import numpy as np

from responsum.response import OGIPResponse, InstrumentResponse
from responsum.utils.package_data import get_path_of_data_file


def test_read_ogip():

    data_file = 'test_n6.rsp'

    path = get_path_of_data_file(data_file)

    ogip_rsp = OGIPResponse(rsp_file=path)




def test_instrument_response():

    nside = 50
    
    matrix = np.identity(nside)

    ebounds = np.range(nside+1)

    mc = np.range(nside+1)

    rsp = InstrumentResponse(matrix,ebounds,mc)

    rsp.plot_matrix()

    rsp.to_fits('test','test','test',overwrite=True)
