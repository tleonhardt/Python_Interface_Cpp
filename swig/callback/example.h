/* File : example.h */

#include <iostream>

class Logger
{
public:
    virtual ~Logger() { std::cout << "Logger::~Logger()" << std:: endl; }
    virtual void log() { std::cout << "Logger::log()" << std::endl; }
};


class Log
{
private:
    Logger *_logger;
public:
    Log(): _logger(nullptr) {}
    ~Log() { delLogger(); }
    void delLogger() { delete _logger; _logger = nullptr; }
    void setLogger(Logger *cb) { delLogger(); _logger = cb; }
    void log() { if (_logger) _logger->log(); }
};

