.data
string1_1: .asciiz "Something went wrong\00"
string2_1: .asciiz "Hello world!\n\00"
string3_1: .asciiz "Hello world!\n\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        li      $8, 5
        sw      $8, 0($fp)
        # BEGIN IF CONDITION
        lw      $8, 0($fp)
        slti    $8, $8, 5
        sw      $8, 4($fp)
        lw      $8, 4($fp)
        beq     $8, $0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string1_1
        li      $2, 4
        syscall 
        # END IF BODY
$L0:    
        # BEGIN IF CONDITION
        lw      $8, 0($fp)
        sge     $8, $8, 5
        sw      $8, 8($fp)
        lw      $8, 8($fp)
        beq     $8, $0, $L1
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string2_1
        li      $2, 4
        syscall 
        # END IF BODY
$L1:    
        # BEGIN IF CONDITION
        lw      $8, 0($fp)
        seq     $8, $8, 5
        sw      $8, 12($fp)
        lw      $8, 12($fp)
        beq     $8, $0, $L3
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        # BEGIN IF CONDITION
        lw      $8, 0($fp)
        sne     $8, $8, 4
        sw      $8, 16($fp)
        lw      $8, 16($fp)
        beq     $8, $0, $L2
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string3_1
        li      $2, 4
        syscall 
        # END IF BODY
$L2:    
        # END IF BODY
$L3:    
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 20($sp)
        lw      $ra, 24($sp)
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $2, 10
        syscall 