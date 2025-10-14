#include "gtest/gtest.h"
#include "part-of-vector.h"
#include <sstream>
#include <fstream>

std::vector<int> get_data(const std::string fname) {
    std::ifstream ifile("../../test/data/" + fname, std::ios::in);
    if (!ifile.good()) {
        std::cerr << "Can't read " << fname << std::endl;
        return {};
    }
    std::vector<int> array;
    int numb;
    while (ifile >> numb) array.push_back(numb);
    return array;
}

std::string read_line(const std::string fname) {
    std::ifstream ifile("../../test/data/" + fname, std::ios::in);
    if (!ifile.good()) {
        std::cerr << "Can't read " << fname << std::endl;
        return {};
    }
    std::string str;
    getline(ifile, str);
    return str;
}

void run_test(const std::string& label) {
    std::ostringstream ioss;
    std::vector<int> v{0, 1, 5, -3, -42, 11};
    auto idata = get_data(label + ".in");
    PrintVectorPart(idata, ioss);
    std::string ostr = read_line(label + ".out");
    ASSERT_EQ(ioss.str(), ostr);
}

TEST(VPart, Simple1) {
   std::ostringstream oss;
   std::vector<int> v{0, 1, 5, -3, -42, 11};
   PrintVectorPart(v, oss);
   ASSERT_EQ(oss.str(), "5 1 0");
}

TEST(VPart, Simple2) {
   std::ostringstream oss;
   std::vector<int> v{0, 1, 5, 3, 42, 11};
   PrintVectorPart(v, oss);
   ASSERT_EQ(oss.str(), "11 42 3 5 1 0");
}

TEST(VPart, Simple3) {
   std::ostringstream oss;
   std::vector<int> v{-1, -5, -3, -42, -11};
   PrintVectorPart(v, oss);
   ASSERT_EQ(oss.str(), "");
}

TEST(VPart, RandomShort) {
    run_test("short");
}

TEST(VPart, RandomMedium) {
    run_test("medium");
}

TEST(VPart, RandomLong) {
    run_test("long");
}

int main(int arc, char **argv) {
    ::testing::InitGoogleTest(&arc, argv);
    return RUN_ALL_TESTS();
}
