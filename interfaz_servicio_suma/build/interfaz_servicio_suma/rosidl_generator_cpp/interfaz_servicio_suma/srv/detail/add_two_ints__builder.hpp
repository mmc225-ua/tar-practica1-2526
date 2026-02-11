// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaz_servicio_suma:srv/AddTwoInts.idl
// generated code does not contain a copyright notice

#ifndef INTERFAZ_SERVICIO_SUMA__SRV__DETAIL__ADD_TWO_INTS__BUILDER_HPP_
#define INTERFAZ_SERVICIO_SUMA__SRV__DETAIL__ADD_TWO_INTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaz_servicio_suma/srv/detail/add_two_ints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaz_servicio_suma
{

namespace srv
{

namespace builder
{

class Init_AddTwoInts_Request_b
{
public:
  explicit Init_AddTwoInts_Request_b(::interfaz_servicio_suma::srv::AddTwoInts_Request & msg)
  : msg_(msg)
  {}
  ::interfaz_servicio_suma::srv::AddTwoInts_Request b(::interfaz_servicio_suma::srv::AddTwoInts_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaz_servicio_suma::srv::AddTwoInts_Request msg_;
};

class Init_AddTwoInts_Request_a
{
public:
  Init_AddTwoInts_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddTwoInts_Request_b a(::interfaz_servicio_suma::srv::AddTwoInts_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_AddTwoInts_Request_b(msg_);
  }

private:
  ::interfaz_servicio_suma::srv::AddTwoInts_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaz_servicio_suma::srv::AddTwoInts_Request>()
{
  return interfaz_servicio_suma::srv::builder::Init_AddTwoInts_Request_a();
}

}  // namespace interfaz_servicio_suma


namespace interfaz_servicio_suma
{

namespace srv
{

namespace builder
{

class Init_AddTwoInts_Response_sum
{
public:
  Init_AddTwoInts_Response_sum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaz_servicio_suma::srv::AddTwoInts_Response sum(::interfaz_servicio_suma::srv::AddTwoInts_Response::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaz_servicio_suma::srv::AddTwoInts_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaz_servicio_suma::srv::AddTwoInts_Response>()
{
  return interfaz_servicio_suma::srv::builder::Init_AddTwoInts_Response_sum();
}

}  // namespace interfaz_servicio_suma

#endif  // INTERFAZ_SERVICIO_SUMA__SRV__DETAIL__ADD_TWO_INTS__BUILDER_HPP_
