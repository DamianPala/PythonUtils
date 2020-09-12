get_filename_component(dir_name ${CMAKE_CURRENT_LIST_DIR} NAME)

createModule(${dir_name} ${CMAKE_CURRENT_LIST_DIR} 
    Sts_Common
)

createModuleTests(${dir_name} ${CMAKE_CURRENT_LIST_DIR} 
    Sts_UnityTtsHelper
    Mock_${dir_name}_ut_mocks
    Sts_Common
)

createMocks(${dir_name}_ut_mocks ${CMAKE_CURRENT_LIST_DIR}/unittests
    ${dir_name}
    Sts_Common
)

addAllSubdirs(${CMAKE_CURRENT_LIST_DIR})
