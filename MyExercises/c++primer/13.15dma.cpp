#include <cstring>
#include "13.14dma.h"

baseDMA::baseDMA(const char * l, int r)
{
    label = new char[strlen(l) + 1];
    strcpy(label, l);
    rating = r;
}

baseDMA::baseDMA(const baseDMA& rs)
{
    label = new char[strlen(rs.label) + 1];
    strcpy(label, rs.label);
    rating = rs.rating;
}

baseDMA::~baseDMA()
{
    delete [] label;
}

baseDMA & baseDMA::operator=(const baseDMA& rs)
{
    if (this == &rs)
        return * this;
    delete [] label;
    label = new char[strlen(rs.label) + 1];
    strcpy(label, rs.label);
    rating = rs.rating;
    return *this;
}

std::ostream & operator<<(std::ostream &os, const baseDMA & rs)
{
    os << "Label: " << rs.label << std::endl;
    os << "Rating: " << rs.rating << std::endl;
    return os;
}

lackDMA::lackDMA(const char* c, const char* l, int r) : baseDMA(l, r)
{
    strncpy(color, c, 39);
    color[39] = '\0';
}

lackDMA::lackDMA(const char* c, const baseDMA& rs) : baseDMA(rs)
{
    strncpy(color, c, COL_LEN - 1);
    color[COL_LEN - 1] = '\0';
}

std::ostream & operator<<(std::ostream & os, const lackDMA & ls)
{
    os << (const baseDMA &) ls;
    os << "Color: " << ls.color << std::endl;
    return os;
}

hasDMA::hasDMA(const char* s, const char* l, int r) : baseDMA(l, r)
{
    style = new char[strlen(s) + 1];
    strcpy(style, s);
}

hasDMA::hasDMA(const char* s, const baseDMA& rs) : baseDMA(rs)
{
    style = new char[strlen(s) + 1];
    strcpy(style, s);
}

hasDMA::hasDMA(const hasDMA& has) : baseDMA(has)
{
    style = new char[strlen(has.style) + 1];
    strcpy(style, has.style);
}

hasDMA::~hasDMA()
{
    delete [] style;
}

hasDMA & hasDMA::operator=(const hasDMA& hs)
{
    if (this == &hs)
        return *this;
    baseDMA::operator=(hs);
    delete [] style;
    style = new char[strlen(hs.style) + 1];
    strcpy(style, hs.style);
    return *this;
}

std::ostream & operator<<(std::ostream & os, const hasDMA & hs)
{
    os << (const baseDMA &) hs;
    os << "Style: " << hs.style << std::endl;
    return os;
}
