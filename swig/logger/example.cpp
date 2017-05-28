/* File : example.cxx */

#include "example.h"

Logger::~Logger()
{
    std::cout << "Logger::~Logger()" << std:: endl;
}

void Logger::log(int level, std::string message)
{
    std::cout << "C++ Logger - Level: ";

    switch(level)
    {
    case LOG_ERROR:
        std::cout << "ERROR";
        break;
    case LOG_WARNING:
        std::cout << "WARNING";
        break;
    case LOG_INFO:
        std::cout << "INFO";
        break;
    default:
        std::cout << "UNKNOWN";
        break;
    }

    std::cout << ",  message: " << message << std::endl;
}
