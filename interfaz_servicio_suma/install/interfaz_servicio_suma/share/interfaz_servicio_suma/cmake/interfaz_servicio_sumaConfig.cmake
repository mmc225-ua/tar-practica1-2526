# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_interfaz_servicio_suma_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED interfaz_servicio_suma_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(interfaz_servicio_suma_FOUND FALSE)
  elseif(NOT interfaz_servicio_suma_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(interfaz_servicio_suma_FOUND FALSE)
  endif()
  return()
endif()
set(_interfaz_servicio_suma_CONFIG_INCLUDED TRUE)

# output package information
if(NOT interfaz_servicio_suma_FIND_QUIETLY)
  message(STATUS "Found interfaz_servicio_suma: 0.0.0 (${interfaz_servicio_suma_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'interfaz_servicio_suma' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${interfaz_servicio_suma_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(interfaz_servicio_suma_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "rosidl_cmake-extras.cmake;ament_cmake_export_dependencies-extras.cmake;ament_cmake_export_include_directories-extras.cmake;ament_cmake_export_libraries-extras.cmake;ament_cmake_export_targets-extras.cmake;rosidl_cmake_export_typesupport_targets-extras.cmake;rosidl_cmake_export_typesupport_libraries-extras.cmake")
foreach(_extra ${_extras})
  include("${interfaz_servicio_suma_DIR}/${_extra}")
endforeach()
