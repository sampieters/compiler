.data
string1_1: .asciiz "Something went wrong\00"
string2_1: .asciiz "Hello world!\0A\00"
string3_1: .asciiz "Hello world!\0A\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -8
        sw      $fp, 8($sp)
        move    $fp, $sp
        li      $8, 5
        sw      $8, 4($fp)
        # BEGIN IF CONDITION
        lw      $9, 0($fp)
        slti    $10, $9, 5
        beq     REGISTER, $0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string1_1
        li      $v0, 4
        syscall 
        # END IF BODY
$L0:    
        # BEGIN IF CONDITION
        lw      $11, 0($fp)
        sgei    $12, $11, 5
        beq     REGISTER, $0, $L1
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string2_1
        li      $v0, 4
        syscall 
        # END IF BODY
$L1:    
        # BEGIN IF CONDITION
        lw      $13, 0($fp)
        seqi    $14, $13, 5
        beq     REGISTER, $0, $L3
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        # BEGIN IF CONDITION
        lw      $24, 0($fp)
        snei    $Error, $24, 4
        beq     REGISTER, $0, $L2
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string3_1
        li      $v0, 4
        syscall 
        # END IF BODY
$L2:    
        # END IF BODY
$L3:    
        nop     
        move    $sp, $fp
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        li      $v0, 10
        syscall 