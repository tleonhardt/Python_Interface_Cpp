/* File : example.h */

#include <iostream>
#include <string>


enum LOG_LEVEL
{
    LOG_INFO = 20,
    LOG_WARNING = 30,
    LOG_ERROR = 40
};


class Logger
{
public:
    virtual ~Logger();
    virtual void log(int level, std::string message);
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
    void log(int level, std::string msg) { if (_logger) _logger->log(level, msg); }
    void err(std::string msg) {log(LOG_ERROR, msg);}
    void war(std::string msg) {log(LOG_WARNING, msg);}
    void inf(std::string msg) {log(LOG_INFO, msg);}
};

