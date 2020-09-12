get_filename_component(dir_name ${CMAKE_CURRENT_LIST_DIR} NAME)

createModule(${dir_name} ${CMAKE_CURRENT_LIST_DIR} 
    Sts_Common
)

createModuleTests(${dir_name} ${CMAKE_CURRENT_LIST_DIR} 
    Sts_UnityTtsHelper
{% if is_mock_header %}    Mock_${dir_name}_ut_mocks
{% endif %}
    Sts_Common
)

{% if is_mock_header %}
createMocks(${dir_name}_ut_mocks ${CMAKE_CURRENT_LIST_DIR}/unittests
    ${dir_name}
    Sts_Common
)

{% endif %}
addAllSubdirs(${CMAKE_CURRENT_LIST_DIR})
