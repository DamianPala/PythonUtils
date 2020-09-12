get_filename_component(dir_name ${CMAKE_CURRENT_LIST_DIR} DIRECTORY)
get_filename_component(dir_name ${dir_name} NAME)

createModule(Ftest_${dir_name} ${CMAKE_CURRENT_LIST_DIR} 
    unity_fixture
    Sts_UnityTtsHelper
    Sts_Common
    Sts_Log
)

addAllSubdirs(${CMAKE_CURRENT_LIST_DIR})
