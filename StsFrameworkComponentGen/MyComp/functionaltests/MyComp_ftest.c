/*=======================================================================================*
 * @file    MyComp_ftest.c
 * @brief   This file contains functional tests for MyComp module.
 *======================================================================================*/

/**
 * @addtogroup MyComp_ftest Description
 * @{
 * @brief Functional tests implementation.
 */

/*======================================================================================*/
/*                       ####### PREPROCESSOR DIRECTIVES #######                        */
/*======================================================================================*/
/*-------------------------------- INCLUDE DIRECTIVES ----------------------------------*/

#include "MyComp_ftest.h"

#include "unity.h"
#include "unity_fixture.h"

#include "Sts_Common.h"
#include "Sts_Log.h"
#include "Sts_UnityTtsHelper.h"

/*----------------------------- LOCAL OBJECT-LIKE MACROS -------------------------------*/

#define RUN_ALL_TESTS
//#define VERBOSE

#define TEST_REPS                                     (5)

/*---------------------------- LOCAL FUNCTION-LIKE MACROS ------------------------------*/

/*======================================================================================*/
/*                      ####### LOCAL TYPE DECLARATIONS #######                         */
/*======================================================================================*/
/*---------------------------- ALL TYPE DECLARATIONS -----------------------------------*/

/*-------------------------------- OTHER TYPEDEFS --------------------------------------*/

/*------------------------------------- ENUMS ------------------------------------------*/

/*------------------------------- STRUCT AND UNIONS ------------------------------------*/

/*======================================================================================*/
/*                    ####### LOCAL FUNCTIONS PROTOTYPES #######                        */
/*======================================================================================*/

static void TestIgnoreCleanup(void);

/*======================================================================================*/
/*                         ####### OBJECT DEFINITIONS #######                           */
/*======================================================================================*/
/*--------------------------------- EXPORTED OBJECTS -----------------------------------*/

/*---------------------------------- LOCAL OBJECTS -------------------------------------*/

STS_LOGGER_CTOR();

TEST_GROUP(MyComp_ftest);

static void (*SetUpSpecyfic)(void);
static void (*TearDownSpecyfic)(void);

/*======================================================================================*/
/*                   ####### LOCAL FUNCTIONS DEFINITIONS #######                        */
/*======================================================================================*/

static void TestIgnoreCleanup(void)
{

}

/*======================================================================================*/
/*                  ####### SETUP AND TEARDOWN DEFINITIONS #######                      */
/*======================================================================================*/

void MyComp_ftest_Init(void (*set_up_specyfic)(void), void (*tear_down_specyfic)(void))
{
    SetUpSpecyfic = set_up_specyfic;
    TearDownSpecyfic = tear_down_specyfic;
}

TEST_SETUP(MyComp_ftest)
{
    STS_UNITY_TTS_HELPER_SETUP();

    /* Set Up your stuff here */
    SetUpSpecyfic();
}

TEST_TEAR_DOWN(MyComp_ftest)
{
    /* Tear down your stuff here */
    TearDownSpecyfic();

    STS_UNITY_TTS_HELPER_TEARDOWN();
}

/*======================================================================================*/
/*                        ####### TESTS DEFINITIONS #######                             */
/*======================================================================================*/

TEST(MyComp_ftest, ICan_DoSomething)
{
    STS_UT_TEST_IGNORE_IF_NOT_RUN_ALL();

    STS_LOG_TEST("I Can do something!");
}

/**
 * @} end of group MyComp_ftest
 */
