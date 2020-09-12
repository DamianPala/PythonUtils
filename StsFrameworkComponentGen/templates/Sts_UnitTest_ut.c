/*=======================================================================================*
 * @file    {{module_name}}_ut.c
 * @brief   This file contains unit tests for {{module_name}} module.
 *======================================================================================*/

/**
 * @addtogroup {{module_name}}_ut Description
 * @{
 * @brief Unit tests implementation.
 */

/*======================================================================================*/
/*                       ####### PREPROCESSOR DIRECTIVES #######                        */
/*======================================================================================*/
/*-------------------------------- INCLUDE DIRECTIVES ----------------------------------*/

#include "unity.h"

#include <pthread.h>
#include <stdatomic.h>
#include <unistd.h>

#include "Sts_Common.h"
#include "Sts_UnityTtsHelper.h"
{% if is_mock_header %}

#include "Mock{{module_name}}_ut_mocks.h"
{% endif %}

#include "{{module_name}}.c"

/*----------------------------- LOCAL OBJECT-LIKE MACROS -------------------------------*/

#define RUN_ALL_TESTS
//#define VERBOSE

#define TEST_REPS                                   (10) // Default: 10

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

STS_LOGGER_CTOR(); // Remove if logger already constructed in .c file

/*======================================================================================*/
/*                   ####### LOCAL FUNCTIONS DEFINITIONS #######                        */
/*======================================================================================*/

static void TestIgnoreCleanup(void)
{
    /* Do Nothing */
}

/*======================================================================================*/
/*                  ####### SETUP AND TEARDOWN DEFINITIONS #######                      */
/*======================================================================================*/

/**
 * @brief   Setup Test Environment.
 */
void setUp(void)
{
    STS_UNITY_TTS_HELPER_SETUP();

    /* Set Up your stuff here */
    {% if is_mock_header %}
    Mock{{module_name}}_ut_mocks_Init();
    {% endif %}
}

/**
 * @brief   Tear Down Test Environment.
 */
void tearDown(void)
{
    /* Tear down your stuff here */
    {% if is_mock_header %}
    Mock{{module_name}}_ut_mocks_Verify();
    {% endif %}

    STS_UNITY_TTS_HELPER_TEARDOWN();
}

/*======================================================================================*/
/*                        ####### TESTS DEFINITIONS #######                             */
/*======================================================================================*/

void test_ICan_DoSomething(void)
{
    STS_UT_TEST_IGNORE_IF_NOT_RUN_ALL();

    STS_LOG_TEST("I Can do something!");
}

void test_ICan_DoSomethingInTestCases(void)
{
    STS_UT_TEST_IGNORE_IF_NOT_RUN_ALL();

    struct testCaseData {
        char * caseName;
        uint32_t inputVar_A;
        uint32_t inputVar_B;
        uint32_t expectedOutputVar_C;
    } testCaseData[] = {
        {
            .caseName = "2 * 3 = 6",
            .inputVar_A = 2,
            .inputVar_B = 3,
            .expectedOutputVar_C = 6
        },
        {
            .caseName = "3 * 8 = 24",
            .inputVar_A = 3,
            .inputVar_B = 8,
            .expectedOutputVar_C = 24
        },
        {
            .caseName = "5 * 2 = 10",
            .inputVar_A = 5,
            .inputVar_B = 2,
            .expectedOutputVar_C = 10
        }
    };

    for (size_t i = 0; i < ARRAY_LEN(testCaseData); i++) {
        struct testCaseData * pTCData = &testCaseData[i];
        char * pMsg = pTCData->caseName;

        uint32_t outputVar_C = pTCData->inputVar_A * pTCData->inputVar_B;
        TEST_ASSERT_EQUAL_MESSAGE(pTCData->expectedOutputVar_C, outputVar_C, pMsg);
    }
}

/**
 * @} end of group {{module_name}}_ut
 */
