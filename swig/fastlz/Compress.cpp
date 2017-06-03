#include "Compress.h"

#include <cstddef>
#include "fastlz.h"

// Intermediate private helper function which wraps fastlz function for compression
static bool _compress(const void *buffer, uint32_t inSize, void *bufOut, uint32_t &sizeOut)
{
    // Has a minimum input buffer size of 16 bytes
    if (inSize < 16)
    {
        return false;
    }

    int ret = fastlz_compress(buffer, inSize, bufOut);
    sizeOut = ret;
    if (0 != ret)
    {
        return true;
    }

    return false;
}

static bool _decompress(const void *buffer, uint32_t inSize, void *bufOut, uint32_t &sizeOut)
{
    int ret = fastlz_decompress(buffer, inSize, bufOut, sizeOut);
    sizeOut = ret;
    if (0 != ret)
    {
        return true;
    }

    return false;
}


// Public functions

bool Compress(const std::vector<uint8_t>& in, std::vector<uint8_t>& out)
{
    size_t N = in.size();

    // Compressed buffer should be *at least* 5% larger than the input buffer
    // We'll err on the side of caution and make it 50% larger
    size_t M = 1.5 * N;

    // Compressed buffer needs to have a minimum size of 66 bytes
    if (M < 66)
    {
        M = 66;
    }

    // If output vector isn't big enough, resize it
    if (out.size() < M)
    {
        out.resize(M);
    }

    // Call file-scope _compress() wrapper around the fastlz function
    bool ok;
    uint32_t compLen = 0;
    ok = _compress(in.data(), N, out.data(), compLen);
    if (ok)
    {
        // Compression succeeded, resize the output vector to correct length
        out.resize(compLen);
    }

    return ok;
}

bool Decompress(const std::vector<uint8_t>& in, std::vector<uint8_t>& out)
{
    // Call the file-scope _decompress() wrapper around the fastlz function
    bool ok;
    uint32_t uncLen = out.size();
    ok = _decompress(in.data(), in.size(), out.data(), uncLen);
    if (ok)
    {
        // Decompression succeeded, resize the output vector to correct length
        out.resize(uncLen);
    }

    return ok;
}
