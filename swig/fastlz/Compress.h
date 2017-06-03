#pragma once

#include <cstdint>
#include <vector>

// Convenience wrappers around fastlz C functions which use STL vectors instead of C arrays

/** Compress an input vector of bytes and store it in an output vector.
 *
 * @param in - std::vector<uint8_t> input vector of uncompressed bytes
 * @param out - std::vector<uint8_t> output vector of compressed bytes
 * @return bool - true if successful, false otherwise
 */
bool Compress(const std::vector<uint8_t>& in, std::vector<uint8_t>& out);

/** Decompress an input vector of bytes and store it in an output vector.
 *
 * @param in - std::vector<uint8_t> input vector of compressed bytes
 * @param out - std::vector<uint8_t> output vector of uncompressed bytes
 * @return bool - true if successful, false otherwise
 */
bool Decompress(const std::vector<uint8_t>& in, std::vector<uint8_t>& out);
