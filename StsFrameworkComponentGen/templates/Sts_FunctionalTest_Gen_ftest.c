/*=======================================================================================*
 * @file    {{module_name}}_ftest.c
 * @brief   This file contains functional tests for {{module_name}} module.
 *======================================================================================*/

/**
 * @addtogroup {{module_name}}_ftest Description
 * @{
 * @brief Functional tests implementation.
 */

/*======================================================================================*/
/*                       ####### PREPROCESSOR DIRECTIVES #######                        */
/*======================================================================================*/
/*-------------------------------- INCLUDE DIRECTIVES ----------------------------------*/

#include "{{module_name}}_ftest.h"

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

TEST_GROUP({{module_name}}_ftest);

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

void {{module_name}}_ftest_Init(void (*set_up_specyfic)(void), void (*tear_down_specyfic)(void))
{
    SetUpSpecyfic = set_up_specyfic;
    TearDownSpecyfic = tear_down_specyfic;
}

TEST_SETUP({{module_name}}_ftest)
{
    STS_UNITY_TTS_HELPER_SETUP();

    /* Set Up your stuff here */
    SetUpSpecyfic();
}

TEST_TEAR_DOWN({{module_name}}_ftest)
{
    /* Tear down your stuff here */
    TearDownSpecyfic();

    STS_UNITY_TTS_HELPER_TEARDOWN();
}

/*======================================================================================*/
/*                        ####### TESTS DEFINITIONS #######                             */
/*======================================================================================*/

TEST({{module_name}}_ftest, ICan_DoSomething)
{
    STS_UT_TEST_IGNORE_IF_NOT_RUN_ALL();

    STS_LOG_TEST("I Can do something!");
}

/**
 * @} end of group {{module_name}}_ftest
 */
