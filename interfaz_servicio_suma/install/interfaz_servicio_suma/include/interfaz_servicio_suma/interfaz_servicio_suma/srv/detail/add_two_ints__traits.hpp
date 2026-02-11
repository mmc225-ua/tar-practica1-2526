// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaz_servicio_suma:srv/AddTwoInts.idl
// generated code does not contain a copyright notice

#ifndef INTERFAZ_SERVICIO_SUMA__SRV__DETAIL__ADD_TWO_INTS__TRAITS_HPP_
#define INTERFAZ_SERVICIO_SUMA__SRV__DETAIL__ADD_TWO_INTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaz_servicio_suma/srv/detail/add_two_ints__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaz_servicio_suma
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddTwoInts_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: a
  {
    out << "a: ";
    rosidl_generator_traits::value_to_yaml(msg.a, out);
    out << ", ";
  }

  // member: b
  {
    out << "b: ";
    rosidl_generator_traits::value_to_yaml(msg.b, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddTwoInts_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "a: ";
    rosidl_generator_traits::value_to_yaml(msg.a, out);
    out << "\n";
  }

  // member: b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "b: ";
    rosidl_generator_traits::value_to_yaml(msg.b, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddTwoInts_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interfaz_servicio_suma

namespace rosidl_generator_traits
{

[[deprecated("use interfaz_servicio_suma::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaz_servicio_suma::srv::AddTwoInts_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaz_servicio_suma::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaz_servicio_suma::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaz_servicio_suma::srv::AddTwoInts_Request & msg)
{
  return interfaz_servicio_suma::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaz_servicio_suma::srv::AddTwoInts_Request>()
{
  return "interfaz_servicio_suma::srv::AddTwoInts_Request";
}

template<>
inline const char * name<interfaz_servicio_suma::srv::AddTwoInts_Request>()
{
  return "interfaz_servicio_suma/srv/AddTwoInts_Request";
}

template<>
struct has_fixed_size<interfaz_servicio_suma::srv::AddTwoInts_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaz_servicio_suma::srv::AddTwoInts_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaz_servicio_suma::srv::AddTwoInts_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace interfaz_servicio_suma
{

namespace srv
{

inline void to_flow_style_yaml(
  const AddTwoInts_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: sum
  {
    out << "sum: ";
    rosidl_generator_traits::value_to_yaml(msg.sum, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AddTwoInts_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: sum
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "sum: ";
    rosidl_generator_traits::value_to_yaml(msg.sum, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AddTwoInts_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interfaz_servicio_suma

namespace rosidl_generator_traits
{

[[deprecated("use interfaz_servicio_suma::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaz_servicio_suma::srv::AddTwoInts_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaz_servicio_suma::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaz_servicio_suma::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaz_servicio_suma::srv::AddTwoInts_Response & msg)
{
  return interfaz_servicio_suma::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaz_servicio_suma::srv::AddTwoInts_Response>()
{
  return "interfaz_servicio_suma::srv::AddTwoInts_Response";
}

template<>
inline const char * name<interfaz_servicio_suma::srv::AddTwoInts_Response>()
{
  return "interfaz_servicio_suma/srv/AddTwoInts_Response";
}

template<>
struct has_fixed_size<interfaz_servicio_suma::srv::AddTwoInts_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaz_servicio_suma::srv::AddTwoInts_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaz_servicio_suma::srv::AddTwoInts_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaz_servicio_suma::srv::AddTwoInts>()
{
  return "interfaz_servicio_suma::srv::AddTwoInts";
}

template<>
inline const char * name<interfaz_servicio_suma::srv::AddTwoInts>()
{
  return "interfaz_servicio_suma/srv/AddTwoInts";
}

template<>
struct has_fixed_size<interfaz_servicio_suma::srv::AddTwoInts>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaz_servicio_suma::srv::AddTwoInts_Request>::value &&
    has_fixed_size<interfaz_servicio_suma::srv::AddTwoInts_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaz_servicio_suma::srv::AddTwoInts>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaz_servicio_suma::srv::AddTwoInts_Request>::value &&
    has_bounded_size<interfaz_servicio_suma::srv::AddTwoInts_Response>::value
  >
{
};

template<>
struct is_service<interfaz_servicio_suma::srv::AddTwoInts>
  : std::true_type
{
};

template<>
struct is_service_request<interfaz_servicio_suma::srv::AddTwoInts_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaz_servicio_suma::srv::AddTwoInts_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFAZ_SERVICIO_SUMA__SRV__DETAIL__ADD_TWO_INTS__TRAITS_HPP_
