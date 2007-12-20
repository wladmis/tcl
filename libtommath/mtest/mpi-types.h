/* Type definitions generated by 'types.pl' */
typedef char               mp_sign;
typedef unsigned short     mp_digit;  /* 2 byte type */
typedef unsigned int       mp_word;   /* 4 byte type */
typedef unsigned int       mp_size;
typedef int                mp_err;

#define MP_DIGIT_BIT       (CHAR_BIT*sizeof(mp_digit))
#define MP_DIGIT_MAX       USHRT_MAX
#define MP_WORD_BIT        (CHAR_BIT*sizeof(mp_word))
#define MP_WORD_MAX        UINT_MAX

#define MP_DIGIT_SIZE      2
#define DIGIT_FMT          "%04X"
#define RADIX              (MP_DIGIT_MAX+1)


/* $Source: /srv/pub/scm/cvs.sf.net/tcl/libtommath/mtest/mpi-types.h,v $ */
/* $Revision: 1.1.1.2 $ */
/* $Date: 2005/09/26 16:32:17 $ */
