"""
`TransBigData`: A Python package develop for transportation spatio-temporal big
data processing, analysis and visualization.

BSD 3-Clause License

Copyright (c) 2021, Qing Yu
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

__version__ = '0.4.17'
__author__ = 'Qing Yu <yuq@sustech.edu.cn>'

# module level doc-string
__doc__ = """
TransBigData - A Python package develop for transportation spatio-temporal big
data processing, analysis and visualization.
=====================================================================

`TransBigData` is a Python package developed for transportation spatio-temporal
big data processing, analysis and visualization. `TransBigData` provides fast
and concise methods for processing common transportation spatio-temporal big
data such as Taxi GPS data, bicycle sharing data and bus GPS data.
`TransBigData` provides a variety of processing methods for each stage of
transportation spatio-temporal big data analysis. The code with `TransBigData`
is clean, efficient, flexible, and easy to use, allowing complex data tasks to
be achieved withconcise code.

For some specific types of data, `TransBigData` also provides targeted tools
for specific needs, such as extraction of Origin and Destination(OD) of taxi
trips from taxi GPS data and identification of arrival and departure
information from bus GPS data. The latest stable release of the software can
be installed via pip and full documentation can be found at
https://transbigdata.readthedocs.io/en/latest/.

Main Features
-------------

Currently, `TransBigData` mainly provides the following methods:

  - Data Quality: Provides methods to quickly obtain the general information of
  the dataset, including the data amount the time period and the sampling
  interval.
  - Data Preprocess: Provides methods to clean multiple types of data error.
  - Data Gridding: Provides methods to generate multiple types of geographic
  grids (Rectangular grids, Hexagonal grids) in the research area. Provides
  fast algorithms to map GPS data to the generated grids.
  - Data Aggregating: Provides methods to aggregate GPS data and OD data into
  geographic polygon.
  - Data Visualization: Built-in visualization capabilities leverage the
  visualization package keplergl to interactively visualize data on Jupyter
  notebook with simple code.
  - Trajectory Processing: Provides methods to process trajectory data,
  including generating trajectory linestring from GPS points, and trajectory
  densification, etc.
  - Basemap Loading: Provides methods to display Mapbox basemap on matplotlib
  figures
"""

from transbigdata.plotmap import (
    plot_map,
    plotscale,
    set_mapboxtoken,
    set_imgsavepath,
    read_imgsavepath,
    read_mapboxtoken
)
from transbigdata.coordinates import (
    gcj02tobd09,
    bd09togcj02,
    wgs84togcj02,
    gcj02towgs84,
    wgs84tobd09,
    bd09towgs84,
    bd09mctobd09,
    getdistance,
    transform_shape
)
from transbigdata.grids import (
    # new
    area_to_grid,
    area_to_params,
    GPS_to_grid,
    grid_to_centre,
    grid_to_polygon,
    grid_to_area,
    grid_to_params,
    grid_params_optimize,
    # old
    rect_grids,
    grid_params,
    grids_centre,
    gridid_sjoin_shape,
    regenerate_params,
    geohash_encode,
    geohash_decode,
    geohash_togrid,
    GPS_to_grids,
    GPS_to_grids_rect,
    GPS_to_grids_tri,
    GPS_to_grids_hexa,
    gridid_to_polygon,
    gridid_to_polygon_rect,
    gridid_to_polygon_tri,
    gridid_to_polygon_hexa
)
from transbigdata.gisprocess import (
    ckdnearest,
    ckdnearest_point,
    ckdnearest_line,
    splitline_with_length,
    merge_polygon,
    polyon_exterior
)
from transbigdata.odprocess import (
    odagg_grid,
    odagg_shape,
    tolinewitharrow
)
from transbigdata.preprocess import (
    clean_same,
    clean_drift,
    clean_outofbounds,
    clean_outofshape,
    clean_traj,
    dataagg,
    id_reindex_disgap,
    id_reindex
)
from transbigdata.bikedata import (
    bikedata_to_od
)
from transbigdata.taxigps import (
    clean_taxi_status,
    taxigps_to_od,
    taxigps_traj_point
)
from transbigdata.mobilephonedata import (
    #new
    mobile_stay_move,
    mobile_stay_dutation,
    mobile_identify_home,
    mobile_identify_work,
    #old    
    traj_stay_move,
    )
from transbigdata.traj import (
    traj_densify,
    traj_sparsify,
    points_to_traj,
    dumpjson
)
from transbigdata.quality import (
    sample_duration,
    data_summary
)
from transbigdata.busgps import (
    busgps_arriveinfo,
    busgps_onewaytime
)
from transbigdata.crawler import (
    getadmin,
    getbusdata,
    get_isochrone_amap,
    get_isochrone_mapbox,
)
from transbigdata.metro import (
    split_subwayline,
    metro_network,
    get_path_traveltime,
    get_shortest_path,
    get_k_shortest_paths
)
from transbigdata.visualization import (
    visualization_trip,
    visualization_od,
    visualization_data
)

from transbigdata.activity import (
    entropy,
    entropy_rate,
    ellipse_params,
    ellipse_plot,
    plot_activity,
    mobile_plot_activity
)